"""
OpenAI /chat/completions → 万象 Anthropic /v1/messages 代理
支持流式和非流式
"""
import json
import asyncio
from aiohttp import web, ClientSession, TCPConnector

ANTHROPIC_BASE = "https://wanqing-api.corp.kuaishou.com/api/gateway/v1/messages"
API_KEY = "iax36glyeuxl5yopgha1dn1v256q74d61qdh"

def openai_to_anthropic(payload: dict) -> dict:
    messages = payload.get("messages", [])
    system_parts = []
    user_messages = []
    
    for msg in messages:
        role = msg.get("role", "")
        if role == "system":
            c = msg["content"]
            system_parts.append(c if isinstance(c, str) else " ".join(x.get("text","") for x in c if isinstance(x,dict)))
        elif role == "assistant" and msg.get("tool_calls"):
            blocks = []
            if msg.get("content"):
                blocks.append({"type": "text", "text": msg["content"]})
            for tc in msg["tool_calls"]:
                args = tc["function"]["arguments"]
                blocks.append({
                    "type": "tool_use",
                    "id": tc["id"],
                    "name": tc["function"]["name"],
                    "input": json.loads(args) if (isinstance(args, str) and args.strip()) else (args if args else {}),
                })
            user_messages.append({"role": "assistant", "content": blocks})
        elif role == "tool":
            user_messages.append({
                "role": "user",
                "content": [{"type": "tool_result", "tool_use_id": msg.get("tool_call_id",""), "content": str(msg.get("content",""))}]
            })
        else:
            user_messages.append(msg)
    
    body = {
        "model": payload["model"],
        "max_tokens": payload.get("max_tokens", 4096),
        "messages": user_messages,
    }
    if system_parts:
        body["system"] = "\n\n".join(system_parts)
    if payload.get("temperature") is not None:
        body["temperature"] = payload["temperature"]
    if payload.get("tools"):
        atools = []
        for t in payload["tools"]:
            if t.get("type") == "function":
                fn = t["function"]
                atools.append({"name": fn["name"], "description": fn.get("description",""), "input_schema": fn.get("parameters", {"type":"object","properties":{}})})
        if atools:
            body["tools"] = atools
    return body

def anthropic_to_openai(data: dict) -> dict:
    blocks = data.get("content", [])
    text = "\n".join(b["text"] for b in blocks if b.get("type") == "text")
    tool_calls = [{"id": b["id"], "type": "function", "function": {"name": b["name"], "arguments": json.dumps(b.get("input",{}))}} for b in blocks if b.get("type") == "tool_use"]
    stop_map = {"end_turn":"stop","max_tokens":"length","tool_use":"tool_calls","stop_sequence":"stop"}
    usage = data.get("usage", {})
    msg = {"role": "assistant", "content": text or None}
    if tool_calls: msg["tool_calls"] = tool_calls
    return {
        "id": data.get("id", ""),
        "object": "chat.completion",
        "model": data.get("model", ""),
        "choices": [{"index": 0, "message": msg, "finish_reason": stop_map.get(data.get("stop_reason",""), "stop")}],
        "usage": {"prompt_tokens": usage.get("input_tokens",0), "completion_tokens": usage.get("output_tokens",0), "total_tokens": usage.get("input_tokens",0)+usage.get("output_tokens",0)}
    }

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "anthropic-version": "2023-06-01",
}

async def handle_chat(request: web.Request):
    body = await request.json()
    is_stream = body.get("stream", False)
    anthropic_body = openai_to_anthropic(body)
    
    if is_stream:
        anthropic_body["stream"] = True
        resp_obj = web.StreamResponse()
        resp_obj.headers["Content-Type"] = "text/event-stream"
        resp_obj.headers["Cache-Control"] = "no-cache"
        await resp_obj.prepare(request)
        
        conn = TCPConnector(ssl=False)
        async with ClientSession(connector=conn) as session:
            async with session.post(ANTHROPIC_BASE, json=anthropic_body, headers=HEADERS) as resp:
                msg_id = "chatcmpl-proxy"
                model_name = body.get("model", "")
                
                # Track tool use state
                current_tool = None
                tool_idx = 0
                
                async for line in resp.content:
                    line = line.decode().strip()
                    if not line or line.startswith(":"):
                        continue
                    if line.startswith("data: "):
                        data_str = line[6:]
                        if data_str == "[DONE]":
                            break
                        try:
                            evt = json.loads(data_str)
                        except:
                            continue
                        
                        etype = evt.get("type", "")
                        chunk = None
                        
                        if etype == "message_start":
                            msg_id = evt.get("message", {}).get("id", msg_id)
                            chunk = {"id": msg_id, "object": "chat.completion.chunk", "model": model_name, "choices": [{"index": 0, "delta": {"role": "assistant", "content": ""}, "finish_reason": None}]}
                        
                        elif etype == "content_block_start":
                            block = evt.get("content_block", {})
                            if block.get("type") == "tool_use":
                                current_tool = {"id": block["id"], "type": "function", "function": {"name": block["name"], "arguments": ""}}
                                chunk = {"id": msg_id, "object": "chat.completion.chunk", "model": model_name, "choices": [{"index": 0, "delta": {"tool_calls": [{"index": tool_idx, "id": block["id"], "type": "function", "function": {"name": block["name"], "arguments": ""}}]}, "finish_reason": None}]}
                        
                        elif etype == "content_block_delta":
                            delta = evt.get("delta", {})
                            if delta.get("type") == "text_delta":
                                chunk = {"id": msg_id, "object": "chat.completion.chunk", "model": model_name, "choices": [{"index": 0, "delta": {"content": delta.get("text", "")}, "finish_reason": None}]}
                            elif delta.get("type") == "input_json_delta":
                                chunk = {"id": msg_id, "object": "chat.completion.chunk", "model": model_name, "choices": [{"index": 0, "delta": {"tool_calls": [{"index": tool_idx, "function": {"arguments": delta.get("partial_json", "")}}]}, "finish_reason": None}]}
                        
                        elif etype == "content_block_stop":
                            if current_tool:
                                tool_idx += 1
                                current_tool = None
                        
                        elif etype == "message_delta":
                            stop_reason = evt.get("delta", {}).get("stop_reason", "")
                            stop_map = {"end_turn":"stop","max_tokens":"length","tool_use":"tool_calls"}
                            finish = stop_map.get(stop_reason, "stop")
                            chunk = {"id": msg_id, "object": "chat.completion.chunk", "model": model_name, "choices": [{"index": 0, "delta": {}, "finish_reason": finish}]}
                        
                        elif etype == "message_stop":
                            break
                        
                        if chunk:
                            await resp_obj.write(f"data: {json.dumps(chunk)}\n\n".encode())
        
        await resp_obj.write(b"data: [DONE]\n\n")
        await resp_obj.write_eof()
        return resp_obj
    
    else:
        conn = TCPConnector(ssl=False)
        async with ClientSession(connector=conn) as session:
            async with session.post(ANTHROPIC_BASE, json=anthropic_body, headers=HEADERS) as resp:
                data = await resp.json(content_type=None)
                if resp.status != 200:
                    return web.json_response({"error": data}, status=resp.status)
                return web.json_response(anthropic_to_openai(data))

async def handle_models(request):
    return web.json_response({"object": "list", "data": [{"id": "ep-ackmqr-1772712498263280527", "object": "model"}]})

app = web.Application()
app.router.add_post("/v1/chat/completions", handle_chat)
app.router.add_post("/chat/completions", handle_chat)
app.router.add_get("/v1/models", handle_models)

if __name__ == "__main__":
    print("🦞 Anthropic Proxy (streaming) running on http://localhost:4000")
    web.run_app(app, host="127.0.0.1", port=4000, print=None)
