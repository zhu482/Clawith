import os
import re
import base64
import argparse
import json

# --- 配置 ---
MD_PATH = "/Users/zhuzhiheng/Desktop/文章/创作空间/普通人怎么学VIBEcoding/隔壁奶奶也能懂：只要会说话，就能做产品 [Vibe指南·02]/隔壁奶奶也能懂：只要会说话，就能做产品 [Vibe指南·02].md"
OUTPUT_HTML = "/Users/zhuzhiheng/Desktop/文章/创作空间/普通人怎么学VIBEcoding/隔壁奶奶也能懂：只要会说话，就能做产品 [Vibe指南·02]/STYLED_ARTICLE_V6_FINAL.html"

# --- 🎨 样式配置 ---
COLOR_RED = "#ab1942"
COLOR_BLACK = "#202124"
COLOR_PROMPT_BG = "#F4F5F7"
COLOR_PROMPT_TEXT = "#37352F"

# 1. 🔮 公众号模式 (Geek Chic)
STYLE_WECHAT = {
    "MODE_NAME": "公众号",
    "BODY": "max-width: 677px; margin: 0 auto; padding: 40px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif; background: #fff;",
    "H1": "display: none;", 
    "H1_DIV": "display: none;",
    "H2": f"font-size: 20px; font-weight: bold; color: {COLOR_BLACK}; margin: 60px 0 24px 0; padding-left: 15px; border-left: 5px solid {COLOR_RED}; line-height: 1.2; letter-spacing: 0.5px;",
    "H3": f"font-size: 17px; font-weight: bold; color: {COLOR_BLACK}; margin: 40px 0 16px 0; display: flex; align-items: center; line-height: 1.5;",
    "H3_ICON": f"<span class='icon' style='color: {COLOR_RED}; font-size: 14px; margin-right: 8px;'>■</span>",
    "P": f"font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 20px; text-align: justify; letter-spacing: 0.5px;",
    "STRONG": f"font-weight: bold; color: {COLOR_BLACK};",
    "NOTE": "color: #9AA0A6; font-style: italic; font-size: 15px;",
    "QUOTE_BOX": f"margin: 30px 0; padding: 20px; background: {COLOR_PROMPT_BG}; border-radius: 8px; color: {COLOR_PROMPT_TEXT}; font-size: 14px; line-height: 1.6; font-family: Consolas, Monaco, monospace;",
    "UL": "margin: 20px 0; padding-left: 20px; list-style-type: none;",
    "LI": "font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px; position: relative; padding-left: 15px;",
    "LI_ICON": f"<span class='icon' style='position: absolute; left: 0; color: {COLOR_RED}; font-weight: bold;'>•</span>",
    "IMG_DIV": "text-align: center; margin: 40px 0; display: block;",
    "IMG": "max-width: 100%; border-radius: 8px; box-shadow: 0 8px 20px rgba(0,0,0,0.08); display: block; margin: 0 auto;",
    "SPACER_DISPLAY": "none" # 公众号靠 P 标签的 margin 来空行，不需要额外的物理空行
}

# 2. 📄 飞书模式 (Raw Clean)
STYLE_FEISHU = {
    "MODE_NAME": "飞书文档",
    "BODY": "margin: 0; padding: 24px; font-family: sans-serif; background: #fff;", 
    "H1": "display: none;", 
    "H1_DIV": "display: none;",
    "H2": "font-size: 1.5em; font-weight: bold; margin: 1.2em 0 0.6em 0; color: #1F2329; border: none; padding: 0;", 
    "H3": "font-size: 1.25em; font-weight: bold; margin: 1.2em 0 0.6em 0; color: #1F2329;",
    "H3_ICON": "", 
    "P": "margin-bottom: 0.8em; line-height: 1.6; color: #1F2329;",
    "STRONG": "font-weight: bold; color: #1F2329;",
    "NOTE": "color: #8F959E; font-style: italic;",
    "QUOTE_BOX": "margin: 1.2em 0; padding: 12px; background: #F5F6F7; border-left: 3px solid #D0D3D6; color: #646A73; font-family: monospace;",
    "UL": "margin: 1em 0; padding-left: 24px; list-style-type: disc;",
    "LI": "margin-bottom: 0.4em; color: #1F2329;",
    "LI_ICON": "", 
    "IMG_DIV": "margin: 1.5em 0;",
    "IMG": "max-width: 100%; display: block;",
    "SPACER_DISPLAY": "block" # 飞书会吞掉 margin，必须显示物理占位符
}

def get_base64_img(img_path):
    try:
        with open(img_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            ext = os.path.splitext(img_path)[1][1:].lower()
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64,{encoded_string}"
    except Exception as e:
        print(f"Error loading image {img_path}: {e}")
        return None

def clean_and_style_text(text):
    text = re.sub(r'\*\*\s+(.*?)\s+\*\*', r'**\1**', text)
    # 完全保留加粗样式
    text = re.sub(r'\*\*(.*?)\*\*', r"<strong class='bold-text'>\1</strong>", text)
    text = re.sub(r'（(.*?)）', r"<span class='note'>（\1）</span>", text) 
    text = re.sub(r'(?<!\])\((.*?)\)', r"<span class='note'>(\1)</span>", text)
    return text

def convert(md_path=MD_PATH, output_path=OUTPUT_HTML):
    if not os.path.exists(md_path): return
    image_dir = os.path.dirname(md_path)

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    S = STYLE_WECHAT 
    html_parts = []
    
    in_ul = False
    in_quote = False
    quote_buffer = []
    paragraph_buffer = []
    empty_line_count = 0
    is_first_h1 = True 

    def flush_paragraph():
        nonlocal paragraph_buffer
        if paragraph_buffer:
            full_text = "<br>".join(paragraph_buffer)
            styled_text = clean_and_style_text(full_text)
            html_parts.append(f"<p class='paragraph' style='{S['P']}'>{styled_text}</p>")
            paragraph_buffer = []

    def flush_quote():
        nonlocal in_quote, quote_buffer
        if quote_buffer:
            # 净化 quote 内部的空白行
            full_quote = "<br>".join([q for q in quote_buffer if q.strip() or q == ""])
            html_parts.append(f"<div class='quote-box' style='{S['QUOTE_BOX']}'>{full_quote}</div>")
            quote_buffer = []
        in_quote = False

    for line in lines:
        raw_line = line.rstrip('\n')
        content = raw_line.strip()

        # 空行处理
        if not content:
            flush_paragraph()
            if in_quote: quote_buffer.append("") 
            if in_ul:
                html_parts.append("</ul>")
                in_ul = False
            empty_line_count += 1
            continue

        # --- 遇到内容的行 ---
        
        # 结算空行 (Spacer Logic)
        if empty_line_count >= 1:
            if not in_quote:
                # 默认隐藏，由 JS 切换。样式上紧凑。
                html_parts.append(f"<p class='spacer' style='display:{S['SPACER_DISPLAY']}; margin:0; line-height:1.6em; min-height:1.6em;'>&nbsp;</p>")
        
        empty_line_count = 0

        # 引用块处理
        if content.startswith(">"):
            flush_paragraph()
            in_quote = True
            quote_buffer.append(content[1:].strip())
            continue
        elif in_quote:
            flush_quote()

        # 特殊块处理
        is_special = (
            content.startswith("#") or 
            content.startswith("![") or 
            content.startswith("- ") or 
            content.startswith("* ") or
            content.startswith("---")
        )

        if is_special:
            flush_paragraph()
            if in_ul and not (content.startswith("- ") or content.startswith("* ")):
                html_parts.append("</ul>")
                in_ul = False

            if content.startswith("- ") or content.startswith("* "):
                if not in_ul:
                    html_parts.append(f"<ul style='{S['UL']}'>")
                    in_ul = True
                li_text = clean_and_style_text(content[2:])
                html_parts.append(f"<li class='list-item' style='{S['LI']}'>{S['LI_ICON']} {li_text}</li>")
            
            elif content.startswith("# "):
                if is_first_h1:
                    is_first_h1 = False
                    continue
                html_parts.append(f"<div class='h1-div' style='{S['H1_DIV']}'><h1 style='{S['H1']}'>{content[2:]}</h1></div>")
            
            elif content.startswith("## "):
                html_parts.append(f"<h2 style='{S['H2']}'>{clean_and_style_text(content[3:])}</h2>")
            elif content.startswith("### "):
                html_parts.append(f"<h3 style='{S['H3']}'>{S['H3_ICON']}{clean_and_style_text(content[4:])}</h3>")
            
            elif content.startswith("!["):
                match = re.search(r'!\[\[(.*?)\]\]', content) or re.search(r'!\[.*?\]\((.*?)\)', content)
                if match:
                    img_src = match.group(1)
                    if img_src.startswith("http"):
                        html_parts.append(f"<div class='img-div' style='{S['IMG_DIV']}'><img src='{img_src}' style='{S['IMG']}'></div>")
                    else:
                        img_path = os.path.join(image_dir, img_src)
                        if os.path.exists(img_path):
                            b64 = get_base64_img(img_path)
                            html_parts.append(f"<div class='img-div' style='{S['IMG_DIV']}'><img src='{b64}' style='{S['IMG']}'></div>")
            
            elif content.startswith("---"):
                html_parts.append("<hr style='border:0; border-top:1px dotted #ccc; margin:40px auto; width:50%;'>")
        
        else:
            paragraph_buffer.append(content)

    # 尾部清理
    flush_paragraph()
    if in_quote: flush_quote()
    if in_ul: html_parts.append("</ul>")

    final_html = f"""
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>Vibe Article Formatter V6.5</title>
        <style>
            .no-select {{ -webkit-user-select: none; user-select: none; }}
            #toolbar {{
                position: fixed; top: 15px; right: 15px; z-index: 10000;
                background: #202124; padding: 6px; border-radius: 40px;
                display: flex; gap: 4px; border: 1px solid #3c4043; box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }}
            .btn {{
                background: transparent; border: none; padding: 6px 14px; border-radius: 20px;
                cursor: pointer; font-size: 13px; color: #bdc1c6; transition: 0.2s;
            }}
            .btn.active {{ background: {COLOR_RED}; color: white; }}
        </style>
    </head>
    <body style="{S['BODY']}" id="article-body">
        <div id="toolbar" class="no-select">
            <button id="btn-wechat" class="btn active" onclick="switchStyle('WECHAT')">公众号模式</button>
            <button id="btn-feishu" class="btn" onclick="switchStyle('FEISHU')">飞书模式</button>
        </div>
        <div id="content">{"".join(html_parts)}</div>
        <script>
            const STYLES = {{"WECHAT": {json.dumps(STYLE_WECHAT)}, "FEISHU": {json.dumps(STYLE_FEISHU)}}};
            function switchStyle(mode) {{
                const s = STYLES[mode];
                const body = document.getElementById('article-body');
                
                document.getElementById('btn-wechat').className = mode === 'WECHAT' ? 'btn active' : 'btn';
                document.getElementById('btn-feishu').className = mode === 'FEISHU' ? 'btn active' : 'btn';
                
                body.style.cssText = s.BODY;
                
                // 核心逻辑：飞书模式显示占位符，公众号模式隐藏占位符
                document.querySelectorAll('.spacer').forEach(el => {{
                    el.style.display = s.SPACER_DISPLAY;
                }});

                document.querySelectorAll('.h1-div, h1').forEach(el => el.style.cssText = (el.tagName === 'H1' ? s.H1 : s.H1_DIV));
                document.querySelectorAll('h2').forEach(el => el.style.cssText = s.H2);
                document.querySelectorAll('h3').forEach(el => {{
                    el.style.cssText = s.H3;
                    const icon = el.querySelector('.icon');
                    if(icon) icon.style.display = (s.H3_ICON === "" ? 'none' : 'inline');
                }});
                document.querySelectorAll('.paragraph').forEach(el => el.style.cssText = s.P);
                document.querySelectorAll('.bold-text').forEach(el => el.style.cssText = s.STRONG);
                document.querySelectorAll('.note').forEach(el => el.style.cssText = s.NOTE);
                document.querySelectorAll('.quote-box').forEach(el => el.style.cssText = s.QUOTE_BOX);
                document.querySelectorAll('ul').forEach(el => el.style.cssText = s.UL);
                document.querySelectorAll('.list-item').forEach(el => {{
                    el.style.cssText = s.LI;
                    const icon = el.querySelector('.icon');
                    if(icon) icon.style.display = (s.LI_ICON === "" ? 'none' : 'inline');
                }});
                document.querySelectorAll('.img-div, img').forEach(el => el.style.cssText = (el.tagName === 'IMG' ? s.IMG : s.IMG_DIV));
            }}
        </script>
    </body>
    </html>
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"✅ V6.5 隔离优化版已生成：\n{output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output")
    args = parser.parse_args()
    input_path = os.path.abspath(args.input)
    output_path = args.output or (os.path.splitext(input_path)[0] + "_STYLED.html")
    convert(input_path, output_path)
