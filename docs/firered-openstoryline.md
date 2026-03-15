# FireRed-OpenStoryline 集成指南

## 项目简介

**FireRed-OpenStoryline** 是一个 AI 视频创作工具，通过对话方式完成短视频剪辑，无需手动操作剪辑软件。

- **GitHub**: https://github.com/FireRedTeam/FireRed-OpenStoryline
- **License**: Apache 2.0
- **要求**: Python ≥ 3.11

### 核心功能

- **智能素材搜索**：自动从网络搜索并下载匹配主题的图片/视频素材
- **智能文案生成**：支持 Few-shot 仿写，精准复制指定风格的语气和句式
- **智能音乐/配音/字体推荐**：根据内容情绪自动匹配 BGM，支持节拍对齐
- **对话式剪辑**：用自然语言描述修改意图，即时输出结果
- **剪辑技能沉淀**：将完整剪辑工作流保存为 Skill，支持批量复用

---

## 安装步骤

### 第一步：克隆项目

```bash
git clone https://github.com/FireRedTeam/FireRed-OpenStoryline.git
cd FireRed-OpenStoryline
```

### 第二步：创建 Python 环境

推荐使用 Conda（建议安装 Miniforge）：

```bash
conda create -n storyline python=3.11
conda activate storyline
```

### 第三步：下载资源 & 安装依赖

#### macOS / Linux（推荐，一键安装）

```bash
sh build_env.sh
```

#### Windows（手动安装）

1. 在项目根目录创建 `.storyline` 文件夹
2. 下载 [models.zip](https://image-url-2-feature-1251524319.cos.ap-shanghai.myqcloud.com/openstoryline/models.zip)，解压到 `.storyline/` 目录
3. 下载 [resource.zip](https://image-url-2-feature-1251524319.cos.ap-shanghai.myqcloud.com/openstoryline/resource.zip)，解压到 `resource/` 目录
4. 安装依赖：`pip install -r requirements.txt`

> **注意**：`models.zip`（约 106MB）和 `resource.zip`（约 426MB）是必须下载的，不包含在 git 仓库中。

---

## 配置文件（config.toml）

项目根目录的 `config.toml` 是核心配置文件，**安装后必须填写**。

### 必填项

```toml
# LLM 模型配置（用于文案生成、理解等）
[llm]
model = "your-model-name"        # 填写模型 ID
base_url = "https://..."         # API 端点 URL
api_key = "your-api-key"         # API Key

# VLM 视觉语言模型配置（用于视频理解）
[vlm]
model = "your-vlm-model"
base_url = "https://..."
api_key = "your-api-key"

# Pexels 素材搜索（搜索在线素材需要）
[search_media]
pexels_api_key = "your-pexels-key"  # 在 https://www.pexels.com/api/ 免费申请
```

### 可选项（TTS 配音）

```toml
# 字节跳动 TTS（可选）
[generate_voiceover.providers.bytedance]
uid = ""
appid = ""
access_token = ""

# MiniMax TTS（可选）
[generate_voiceover.providers.minimax]
base_url = "https://..."
api_key = ""
```

### MCP Server 端口（如有冲突可修改）

```toml
[local_mcp_server]
port = 8001  # 默认 8001，如端口被占用可改为其他端口
```

详细配置说明参考官方文档：[API Key Configuration](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/docs/source/en/api-key.md)

---

## 启动方式

### 标准启动（两步）

**第一步：启动 MCP Server**

```bash
# macOS / Linux
PYTHONPATH=src python -m open_storyline.mcp.server

# Windows
$env:PYTHONPATH="src"; python -m open_storyline.mcp.server
```

**第二步：启动对话界面**

```bash
# 方式 A：命令行
python cli.py

# 方式 B：Web 界面（访问 http://127.0.0.1:8005）
uvicorn agent_fastapi:app --host 127.0.0.1 --port 8005
```

### Docker 启动

```bash
# 国内用户推荐阿里云镜像
docker pull crpi-6knxem4w8ggpdnsn.cn-shanghai.personal.cr.aliyuncs.com/openstoryline/openstoryline:v1.0.0

docker run \
  -v $(pwd)/config.toml:/app/config.toml \
  -v $(pwd)/outputs:/app/outputs \
  -p 7860:7860 \
  openstoryline/openstoryline:v1.0.0
# 访问 http://0.0.0.0:7860
```

---

## 与 Clawith 集成

FireRed-OpenStoryline 支持通过 Claude Code Skills 调用。

### 方式一：从项目根目录使用（推荐）

在 FireRed-OpenStoryline 项目根目录启动 Claude Code，直接使用内置 Skill：

```bash
/openstoryline-install   # 首次安装和配置
```

### 方式二：安装到全局 Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R .claude/skills/openstoryline-install ~/.claude/skills/
```

### 方式三：OpenClaw

```bash
npm i -g clawhub
clawhub install openstoryline-install
clawhub install openstoryline-use
```

---

## 本机现有安装位置

> 本节记录项目已在本机的实际安装状态，方便下次恢复。

- **代码位置**：`~/Desktop/Clawith-main/backend/agent_data/2773da9f-.../workspace/workspace/FireRed-OpenStoryline/`
- **资源状态**：`resource.zip`（426MB）和 `models.zip`（106MB）已下载，`resource/` 已解压
- **模型**：TransNetV2 权重已下载至 `.storyline/models/`
- **环境**：Python 环境已配置，依赖已安装

> **注意**：以上路径中的文件不在 Clawith git 仓库中（被 `.gitignore` 排除）。重新部署时需按上方步骤重新安装。

---

## 参考文档

- [官方 README](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/README.md)
- [API Key 配置](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/docs/source/en/api-key.md)
- [使用教程](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/docs/source/en/guide.md)
- [常见问题](https://github.com/FireRedTeam/FireRed-OpenStoryline/blob/main/docs/source/en/faq.md)
- [HuggingFace Demo](https://fireredteam-firered-openstoryline.hf.space/)
