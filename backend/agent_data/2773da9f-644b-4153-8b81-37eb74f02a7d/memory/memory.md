# 龙虾导演 — 长期记忆

## 关键配置
- **Pexels API Key**: dhVW3mdCI548sxGYZ9CvQvaKPHAAerbF8TIXzcFzxNuF1OUUS86j2OkJ
- **阿里云百炼 TTS API Key**: sk-d9e0a59335d141f9b9d11a82f7cd6eaf

## 核心工作流：多模态分块对齐自动化剪辑架构 (Chunk-based Alignment)
与 zzh 确认的最新视频生成框架。核心原则：“音频定长，画面自适应，逐句封装，最后拼接。”

**执行步骤：**
1. **剧本颗粒化拆解**：将口播稿按句/意群拆分为独立的“分镜单元 (Scene)”。
2. **多模态素材打点**：
   - 爬取原链接图、搜索视频(yt-dlp)、或使用 Pexels 补充。
   - 使用万象多模态大模型 (`ep-3vrrg5-1772715777505520100` + `OPENAI_API_KEY`) 分析长素材，精准选出契合当前句子的画面起止时间戳。
3. **音频合成与绝对时长确立**：
   - 使用阿里云百炼 TTS (模型: `qwen3-tts-flash`) 为当前 Scene 单独生成音频。
   - 调用代码示例 (Python):
     ```python
     import os
     import dashscope
     dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'
     response = dashscope.audio.qwen_tts.SpeechSynthesizer.call(
         model="qwen3-tts-flash",
         api_key="sk-d9e0a59335d141f9b9d11a82f7cd6eaf",
         text="单句文案",
         voice="Cherry", # 可根据角色调整音色
         language_type="Chinese",
         stream=False
     )
     ```
   - 获取音频绝对物理时长 `T`。
4. **画面裁剪与强制对齐**：使用 FFmpeg 将大模型选出的画面强制适配时长 `T`（截断、变速或循环），并压制单句硬字幕，生成独立的 `clip_scene_N.mp4`。
5. **无缝拼接与双端输出**：将所有单句片段无缝拼接 (concat)，加上 BGM 和全局特效，输出 B站版 (16:9) 和 短视频版 (9:16)。

## 配图/素材搜集策略
- **首选**：爬取稿件原链接中的网页截图/核心图片。
- **次选**：根据段落主题，使用 `web_search`/`jina_search` 搜索并在代码沙箱中用 `yt-dlp` 下载 B站/YouTube 相关视频片段。
- **兜底**：Pexels 免版权库（内容相关性较差，仅作空镜补充）。
