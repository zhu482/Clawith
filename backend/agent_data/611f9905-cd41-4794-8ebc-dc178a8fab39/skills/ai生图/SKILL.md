---
name: image-generator
description: 纯粹的AI图片生成与编辑工具。支持文生图和图生图（编辑），基于 Gemini 3 Pro Image API。无预设风格，完全根据用户需求生成。
version: 1.0.0
trigger_keywords: ["生图", "AI绘画", "图片生成", "图片编辑", "图生图", "文生图"]
---

# AI生图 - 自由创作工具

## 功能定位
纯粹的 AI 图片生成与编辑工具，**不依赖文章内容**，支持自由创作。

与其他技能的区别：
- **概念可视化**：专注于知识卡片，有固定的白板手绘风格
- **AI生图**：纯粹的生图工具，无预设风格，完全自由

---

## 核心功能

### 1. 文生图（纯文字描述）
根据文字描述直接生成图片。

**使用场景**：
- 概念设计快速可视化
- 为文章、视频创作配图
- UI/UX 设计的快速原型
- 自由艺术创作

**示例**：
```bash
python3 .agent/skills-v2/04-视觉设计/AI生图/scripts/generate.py \
  --prompt "未来科技感的智能家居控制面板,深色主题,玻璃拟态设计" \
  --output "smart_home_ui.jpg" \
  --aspect-ratio "16:9" \
  --quality "high"
```

---

### 2. 图生图（编辑现有图片）
基于现有图片进行编辑和修改。

**使用场景**：
- 修改图片背景
- 风格转换
- 局部编辑

**示例**：
```bash
python3 .agent/skills-v2/04-视觉设计/AI生图/scripts/generate.py \
  --prompt "保持人物不变,将背景改为星空" \
  --input "portrait.jpg" \
  --output "portrait_starry.jpg"
```

---

### 3. 多图合成
支持最多3张图片的组合编辑。

**示例**：
```bash
python3 .agent/skills-v2/04-视觉设计/AI生图/scripts/generate.py \
  --prompt "将这两张图片合成一张,左右排列" \
  --input "image1.jpg" "image2.jpg" \
  --output "combined.jpg"
```

---

## 参数说明

### 必需参数
- `--prompt`: 文字描述或编辑指令
- `--output`: 输出文件路径

### 可选参数
- `--input`: 输入图片路径（支持1-3张）
- `--aspect-ratio`: 图片比例
  - `1:1` (默认)
  - `16:9` (横屏)
  - `9:16` (竖屏)
  - `4:3`
  - `3:4`
- `--quality`: 画质
  - `standard` (默认)
  - `high` (高清)
  - `ultra` (超高清)

---

## API 配置

- **Base URL**: `https://poloai.top/v1beta/models/gemini-3-pro-image-preview:generateContent`
- **API Key**: `sk-UwODXWv3MMlvC01sWiOohl9MgO1QkcCGxWCjsEdtiQs500HO`
- **官方文档**: https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn

---

## 输出目录

生成的图片默认保存在：`创作空间/AI生图/`

---

## 注意事项

1. 输入图片会自动转换为 Base64 编码
2. 支持的图片格式：JPG, PNG, WEBP
3. 单次最多支持 3 张输入图片
4. 生成时间取决于图片复杂度和画质设置
5. API 有调用频率限制，请合理使用

---

## 技术细节

- 使用 Gemini 3 Pro Image Preview 模型
- 支持多模态输入（文字 + 图片）
- 自动处理图片编码和 API 调用
- 错误处理和重试机制
