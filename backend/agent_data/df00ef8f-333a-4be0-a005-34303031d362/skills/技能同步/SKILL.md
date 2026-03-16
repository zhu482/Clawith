---
name: skill-sync
description: 技能同步工具。将技能从单一数据源同步到多个IDE/CLI平台,确保所有平台技能保持一致。
trigger_keywords: [同步技能, 技能同步, 更新技能, publish, sync, 发布技能]
version: 2.0.0
---

# skill-sync - 技能同步工具

## 功能说明

自动将技能从单一数据源同步到多个 IDE/CLI 平台，确保所有平台的技能保持一致。

## 平台架构

### 数据源（Source of Truth）
- **`.codeflicker/skills/`** - 所有技能的唯一数据源
  - 使用目录结构：每个技能一个文件夹
  - 每个技能包含 `SKILL.md` 文件

### 同步目标平台

1. **Antigravity/Agent** (`.agent/skills/`)
   - 格式：目录结构
   - 路径：`.agent/skills/<skill-name>/SKILL.md`

2. **Claude** (`.claude/skills/`)
   - 格式：扁平化文件结构
   - 路径：`.claude/skills/<skill-name>.md`

3. **Kiro** (`.kiro/steering/`)
   - 格式：扁平化文件结构，使用中文命名
   - 路径：`.kiro/steering/技能_<中文名>.md`
   - 特例：`core-guidelines` 使用 `核心规范.md`（无"技能_"前缀）

## 使用方法

### 同步所有技能
```bash
python3 .codeflicker/skills/sync_skills.py --all
```

### 同步单个技能
```bash
python3 .codeflicker/skills/sync_skills.py --skill writing
```

### 同步多个技能
```bash
python3 .codeflicker/skills/sync_skills.py --skill writing --skill memory
```

### 预览同步操作（不实际执行）
```bash
python3 .codeflicker/skills/sync_skills.py --all --dry-run
```

## 工作流程

1. **编辑技能**：在 `.codeflicker/skills/<skill-name>/SKILL.md` 中修改技能内容
2. **运行同步**：执行同步脚本
3. **自动分发**：脚本会自动将更新同步到所有平台
4. **验证结果**：检查各平台的技能文件是否正确更新

## 技能名称映射

| 英文名称 | Kiro 中文名称 |
|---------|-------------|
| core-guidelines | 核心规范 |
| diary | 日记 |
| memory | 记忆 |
| retrieval | 检索 |
| style-learning | 风格学习 |
| topic-deepening | 选题深化 |
| vector-manager | 向量 |
| wechat-manager | 公众号 |
| writing | 写作 |
| xiaohongshu-draft | 小红书文稿 |
| xiaohongshu-layout | 小红书排版 |
| skill-sync | 技能同步 |

## 安全规则

- ✅ 只覆盖目标技能文件
- ✅ 自动创建不存在的目录
- ❌ 永不删除目标目录
- ⚠️ 如果目标文件有本地定制内容，请先将其合并到源技能中

## 智能检测

同步脚本会自动：
- 检测 `.codeflicker/skills/` 下的所有技能目录
- 跳过非技能文件（README.md、脚本文件等）
- 确保所有平台目录存在
- 处理不同平台的命名约定

## 注意事项

1. **单向同步**：只从 `.codeflicker/skills/` 同步到其他平台，不支持反向同步
2. **覆盖写入**：同步会完全覆盖目标文件，请确保源文件是最新的
3. **编码一致**：所有文件使用 UTF-8 编码
4. **自我同步**：`skill-sync` 技能本身也会被同步到所有平台
