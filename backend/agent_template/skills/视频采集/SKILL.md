---
name: video-hunter
description: 全能视频猎手。跨平台视频内容抓取、转写、归档，支持B站/抖音/小红书/快手等7大平台。
version: 2.0.0
trigger_keywords: ["视频采集", "下载视频", "爬取视频", "视频转写", "抓取视频", "采集视频", "视频搜索"]
---

# Video Hunter (全能视频猎手)

## 技能描述
这是您内容生产流程的**万能中枢**。它无缝集成了 **MediaCrawler** 的所有强大功能，并在任务完成后自动执行**资源归档**和**AI语音转写**。

一键完成：**爬取 -> 整理 -> 转写**。

## 核心功能
*   **先搜后看**: 默认抓取信息并返回 **Markdown 表格**供您查阅（包含标题、作者、链接等）。
*   **智能归档**: 使用 `--download` 下载并处理后，默认只保留 **Markdown 文档** (含转写内容+点赞/收藏等数据)，自动清理庞大的视频/音频文件，节省空间。
*   **完整保留**: 如需保留原始视频/音频，可添加 `--keep-media` 参数。
*   **数据丰富**: 自动提取 **点赞、收藏、评论、转发、观看** 等核心指标并在文档头部展示。
*   **全平台支持**: B站 (bili)、抖音 (dy)、小红书 (xhs)、快手 (ks)、微博 (wb)、贴吧 (tieba)、知乎 (zhihu)。

## 使用方法

### 基本语法
```bash
python .agent/skills/video-hunter/hunt_video.py [关键词/ID] [选项...]
```

### 常用命令示例

#### 1. 关键词搜索 (预览模式)
仅返回列表，不下载文件。
```bash
python .agent/skills/video-hunter/hunt_video.py "AI Agent教程"
```

#### 2. 下载并生成文档 (默认模式: MD Only)
下载视频 -> 转写 -> 生成含数据的 MD -> **删除视频/音频**。
```bash
python .agent/skills/video-hunter/hunt_video.py "BV1xx411c7mD" --type detail --download
```

#### 3. 下载并保留素材 (完整模式)
下载视频 -> 转写 -> 生成含数据的 MD -> **保留视频/音频**。
```bash
python .agent/skills/video-hunter/hunt_video.py "BV1xx411c7mD" --type detail --download --keep-media
```

#### 4. 爬取博主主页 (小红书)
```bash
python .agent/skills/video-hunter/hunt_video.py "5ad...userid" --platform xhs --type creator --count 50
```

## 参数说明
*   `query`: (必填) 搜索关键词 或 视频ID/用户ID。
*   `--download`: 开启下载与转写流程。
*   `--keep-media`: **保留** 视频与音频原文件 (默认处理完后会自动删除)。
*   `--platform`: 目标平台 (bili, dy, xhs, ks, wb, tieba, zhihu)。默认 `bili`。
*   `--type`: 操作类型 (search, detail, creator)。默认 `search`。
*   `--count`: 爬取数量限制 (仅 Search/Creator)。默认 `20`。
*   `--login-type`: 登录方式 (qrcode, phone, cookie)。默认 `qrcode`。
*   `--cookies`: Cookie 登录时的 Cookie 字符串。
*   `--headless`: 强制开启无头模式（不弹窗）。
*   `--no-headless`: 强制关闭无头模式（如需扫码）。
*   `--get-comment`: 是否爬取一评论。默认 `否`。
*   `--get-sub-comment`: 是否爬取二级评论。默认 `否`。
*   `--max-comments`: 每个视频/帖子的一级评论数量限制。默认 `10`。
*   `--start-page`: 起始页码。默认 `1`。
*   `--max-concurrency`: 并发爬虫数量。默认 `1`。

## 文件保存结构
脚本执行后，资源将保存至 `视频资源/` 目录下（或指定 output-dir），结构如下：

*   **关键词搜索模式**:
    `视频资源/<平台>/<搜索关键词>/<日期>_<视频标题>/...`
    
*   **指定作者/视频模式**:
    `视频资源/<平台>/<作者昵称>/<日期>_<视频标题>/...`

目录下包含：
*   `README.md`: 完整文档 (含转写与数据)
*   `video.mp4`: 原始视频 (仅 `--keep-media` 模式)
*   `audio_extracted.mp3`: 提取音频 (仅 `--keep-media` 模式)
*   `metadata.json`: 原始元数据

## 依赖说明
*   `MediaCrawler/`
*   `视频资源/organize_media.py`
*   `视频资源/transcribe.py`

---
*Created by Gemini Agent*
