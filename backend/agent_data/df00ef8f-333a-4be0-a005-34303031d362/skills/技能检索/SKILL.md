---
name: skill-discovery
description: Claude Skills 检索与安装助手。帮助用户发现、搜索、安装和管理 Claude/Agent 技能。
trigger_keywords: [技能检索, 搜索技能, 安装技能, 发现技能, skill discovery, find skills, claude skills]
version: 2.0.0
---

# 技能检索 - Skill Discovery

帮助用户发现、搜索、安装和管理 Claude/Agent 技能的完整工具。

## 核心功能

### 1. 技能来源汇总

用户可以从以下渠道获取技能：

#### A. GitHub 官方仓库 ⭐ 推荐

**1. Anthropic 官方技能库** ⭐ 67,634 stars
- **仓库**: https://github.com/anthropics/skills
- **描述**: Anthropic 公开的官方 Agent Skills 仓库
- **特点**: 官方维护、质量保证、持续更新
- **安装**:
  ```bash
  # Claude Desktop / Code
  claw skill add anthropics/skills
  
  # 交互式选择
  claw skill add -i anthropics/skills
  ```

**2. Awesome OpenClaw Skills** ⭐ 13,268 stars
- **仓库**: https://github.com/VoltAgent/awesome-openclaw-skills
- **描述**: OpenClaw Skills 精选集合（前身：Moltbot, Clawdbot）
- **特点**: 社区精选、分类清晰、定期维护
- **分类包含**:
  - PDF & Documents
  - Code & Development
  - Writing & Content
  - Data & Analytics
  - 等多个分类
- **安装**:
  ```bash
  claw skill add VoltAgent/awesome-openclaw-skills
  ```

**3. Everything Claude Code** ⭐ 43,815 stars
- **仓库**: https://github.com/affaan-m/everything-claude-code
- **描述**: 完整的 Claude Code 配置集合
- **包含**: agents, skills, hooks, commands, rules, MCPs
- **特点**: Anthropic 黑客马拉松获奖者的实战配置
- **安装**:
  ```bash
  claw skill add affaan-m/everything-claude-code
  ```

#### B. 技能市场

**SKILLS.pub**
- **网站**: https://skills.pub/zh
- **描述**: 第三方 Claude Skills 市场
- **内容**: 300+ 技能库
- **功能**:
  - 浏览和探索技能
  - 查看技能详情和 GitHub 仓库
  - 提交新技能
  - 学习资源和文档

**使用方法**:
1. 访问 https://skills.pub/zh
2. 浏览找到需要的技能
3. 点击查看 GitHub 仓库
4. 复制仓库地址（格式：`user/repo`）
5. 使用命令安装：
   ```bash
   claw skill add user/repo
   ```

#### C. 本地项目技能

**位置**: `.agent/skills/` 或 `.claude/skills/`

**当前项目的技能架构**:
```
.agent/skills/
├── 00-系统核心/
├── 01-内容创作/
├── 02-商业咨询/
├── 03-用户研究/
├── 04-视觉设计/
├── 05-内容工具/
└── 06-工作辅助/
```

#### D. 全局技能目录

**位置**: 
- `~/.claw/skills/` (OpenClaw)
- `~/.claude/skills/` (Claude Desktop)
- `~/.agent/skills/` (其他 Agent 框架)

**安装到全局**:
```bash
claw skill add -g user/repo
```

---

## 使用指南

### 1. 搜索技能

#### 在 GitHub 上搜索
```bash
# 搜索 Claude Skills
https://github.com/search?q=claude+skill&sort=stars

# 搜索特定主题
https://github.com/search?q=claude+skill+writing
https://github.com/search?q=claude+skill+code-review
https://github.com/search?q=agent+skill+pdf
```

#### 查看本地已安装技能
```bash
# 列出所有技能
claw skill list

# 以 JSON 格式输出
claw skill list --json

# 查看特定目录的技能
claw skill list --target .agent/skills
```

---

### 2. 安装技能

#### 基础安装
```bash
# 从 GitHub 安装
claw skill add user/repo

# 从子目录安装
claw skill add user/repo/skills/writing
 交互式选择（推荐）
claw skill add -i user/repo
```

#### 高级安装选项

**自定义名称**:
```bash
claw skill add --name my-custom-name user/repo
```

**覆盖已存在的技能**:
```bash
claw skill add --overwrite user/repo
```

**安装到不同位置**:
```bash
# 安装到全局
claw skill add -g user/repo

# 安装到 Claude Desktop
claw skill add --claude user/repo

# 安装到自定义目录
claw skill add --target ./custom/path user/repo
```

**组合使用**:
```bash
# 交互式选择 + 全局安装
claw skill add -i -g user/repo

# 自定义名称 + Claude
claw skill add --claude --name my-skill user/repo
```

---

### 3. 管理技能

#### 删除技能
```bash
# 删除项目技能
claw skill remove my-skill

# 删除全局技能
claw skill remove -g my-skill

# 从自定义目录删除
claw skill remove --target ./custom/path my-skill
```

#### 更新技能
```bash
# 重新安装（使用 --overwrite）
claw skill add --overwrite user/repo
```

---

## 技能发现策略

### 推荐技能市场

#### 1. Anthropic 官方 ⭐ 最推荐
**仓库**: https://github.com/anthropics/skills

**为什么选择官方仓库**:
- ✅ Anthropic 官方维护
- ✅ 质量保证
- ✅ 持续更新
- ✅ 安全可靠

**安装方式**:
```bash
# 查看所有可用技能
claw skill add -i anthropics/skills

# 直接安装所有
claw skill add anthropics/skills

# 安装到全局
claw skill add -g anthropics/skills
```

#### 2. Awesome OpenClaw Skills ⭐ 社区精选
**仓库**: https://github.com/VoltAgent/awesome-openclaw-skills

**特点**:
- 📚 分类清晰（PDF/Code/Writing/Data等）
- 🌟 社区精选
- 🔄 定期维护
- 📖 详细文档

**安装方式**:
```bash
# 交互式选择
claw skill add -i VoltAgent/awesome-openclaw-skills

# 安装所有
claw skill add VoltAgent/awesome-openclaw-skills
```

#### 3. SKILLS.pub
**网站**: https://skills.pub/zh

**使用方法**:
1. 访问网站浏览 300+ 技能
2. 找到需要的技能
3. 点击查看 GitHub 仓库
4. 复制仓库地址
5. 使用 `claw skill add user/repo` 安装

**热门技能**:
- `create-pr` - 创建 Pull Request
- `concept-workflow` - 概念工作流

#### 4. Everything Claude Code
**仓库**: https://github.com/affaan-m/everything-claude-code

**包含内容**:
- Agents - 智能代理配置
- Skills - 实战技能包
- Hooks - 自定义钩子
- Commands - 命令集合
- Rules - 规则配置
- MCPs - MCP 服务器配置

### GitHub 搜索关键词

#### 按功能分类
- `claude skill writing` - 写作相关
- `claude skill code-review` - 代码审查
- `claude skill testing` - 测试相关
- `claude skill documentation` - 文档生成
- `claude skill refactoring` - 重构工具
- `agent skill pdf` - PDF 处理
- `agent skill data` - 数据分析

#### 按编程语言
- `claude skill python`
- `claude skill javascript`
- `claude skill typescript`
- `claude skill rust`

#### 按应用场景
- `claude skill debugging` - 调试
- `claude skill deployment` - 部署
- `claude skill monitoring` - 监控
- `claude skill security` - 安全

---

## 技能目录结构规范

### 标准技能目录结构
```
skill-name/
├── SKILL.md              # 技能定义（必需）
├── README.md             # 说明文档（可选）
├── scripts/              # 脚本文件（可选）
│   └── *.py
└── examples/             # 示例文件（可选）
    └── *.md
```

### SKILL.md 最小要求
```markdown
---
name: skill-name
description: 技能描述
trigger_keywords: [关键词1, 关键词2]
version: 1.0.0
---

# 技能名称

技能内容...
```

---

## 常见问题

### Q1: 如何创建自己的技能？
1. 创建目录和 `SKILL.md` 文件
2. 定义 frontmatter（name, description, trigger_keywords）
3. 编写技能内容
4. 推送到 GitHub 公开仓库
5. 使用 `claw skill add user/repo` 安装

### Q2: 技能安装后在哪里？
- 默认：`.agent/skills/skill-name/` 或 `.claude/skills/skill-name/`
- 全局：`~/.claw/skills/skill-name/` 或 `~/.claude/skills/skill-name/`
- Claude Desktop：`.claude/skills/skill-name.md`（扁平化）

### Q3: 如何分享技能给其他人？
1. 将技能推送到 GitHub 公开仓库
2. 分享仓库地址：`user/repo`
3. 其他人使用 `claw skill add user/repo` 安装
4. 可选：提交到 SKILLS.pub 市场

### Q4: 技能冲突怎么办？
使用 `--name` 参数自定义本地名称：
```bash
claw skill add --name my-writing user/repo/writing
```

### Q5: 如何查看技能是否安装成功？
```bash
# 列出所有技能
claw skill list

# 检查特定目录
ls -la .agent/skills/
ls -la .claude/skills/
```

### Q6: 不同的 CLI 命令有什么区别？
- `claw` - OpenClaw/Claude Code 通用命令
- `claude` - Claude Desktop 专用
- `agent` - 其他 Agent 框架

根据你使用的工具选择对应命令。

---

## 技能生态推荐

### 官方仓库 ⭐ 最推荐
1. **Anthropic Skills** - anthropics/skills
   - ⭐ 67,634 stars
   - 官方维护
   - 质量保证

2. **Awesome OpenClaw Skills** - VoltAgent/awesome-openclaw-skills
   - ⭐ 13,268 stars
   - 社区精选
   - 分类清晰

### 社区仓库
3. **Everything Claude Code** - affaan-m/everything-claude-code
   - ⭐ 43,815 stars
   - 完整配置集合
   - 实战经验

### 技能市场
4. **SKILLS.pub** - https://skills.pub/zh
   - 300+ 技能库
   - 精选展示
   - 可提交新技能

### GitHub 搜索技巧
```bash
# 按星标排序查找热门技能
https://github.com/search?q=claude+skill&sort=stars
https://github.com/search?q=agent+skill&sort=stars

# 搜索特定类型
https://github.com/search?q=claude+skill+writing
https://github.com/search?q=agent+skill+pdf
```

---

## 最佳实践

### 1. 优先选择官方和高星仓库
```bash
# 推荐顺序
1. anthropics/skills (官方)
2. VoltAgent/awesome-openclaw-skills (社区精选)
3. affaan-m/everything-claude-code (实战配置)
4. SKILLS.pub (市场浏览)
```

### 2. 使用交互式安装
```bash
# 推荐使用 -i 参数
claw skill add -i user/repo

# 好处：
# - 可以预览所有可用技能
# - 选择性安装需要的技能
# - 避免安装不需要的技能
```

### 3. 分类管理技能
```bash
# 项目专用技能 → .agent/skills/ 或 .claude/skills/
# 通用技能 → 全局目录
# 团队共享 → Git 仓库管理
```

### 4. 定期更新技能
```bash
# 检查技能仓库的更新
# 使用 --overwrite 重新安装
claw skill add --overwrite user/repo
```

### 5. 文档化你的技能栈
在项目 README 中记录使用的技能：
```markdown
## 技能依赖
- writing (anthropics/skills/writing)
- code-review (VoltAgent/awesome-openclaw-skills/code-review)
- custom-skill (本地开发)
```

---

## 技能开发指南

### 创建技能的最佳实践

#### 1. 命名规范
- 使用小写字母和连字符：`my-skill`
- 避免过于通用的名称
- 清晰表达技能功能

#### 2. 描述清晰
```yaml
---
name: skill-name
description: 一句话说明技能用途和核心价值
trigger_keywords: [精确的触发词, 不要太泛化]
version: 1.0.0
---
```

#### 3. 结构化内容
- 使用 Markdown 标题组织内容
- 提供使用示例
- 说明前置条件和依赖

#### 4. 包含测试用例
- 在 `examples/` 目录提供示例
- 说明预期输入和输出
- 提供常见问题解答

### 如何贡献技能

#### 贡献到官方仓库
1. Fork `anthropics/skills`
2. 添加你的技能到合适的目录
3. 提交 Pull Request
4. 等待 Anthropic 团队审核

#### 贡献到社区仓库
1. Fork `VoltAgent/awesome-openclaw-skills`
2. 在对应分类添加技能
3. 更新 README.md
4. 提交 Pull Request

#### 提交到 SKILLS.pub
1. 访问 https://skills.pub/zh
2. 点击"提交新的 Skills"
3. 填写技能信息和 GitHub 链接
4. 等待审核

---

## 技能检索命令速查

```bash
# === 搜索 ===
claw skill list                    # 列出本地所有技能
claw skill list --json             # JSON 格式输出

# === 安装 ===
claw skill add user/repo           # 基础安装
claw skill add -i user/repo        # 交互式安装（推荐）
claw skill add -g user/repo        # 全局安装
claw skill add --claude user/repo  # 安装到 Claude Desktop
claw skill add --name my user/repo # 自定义名称
claw skill add --overwrite user/repo # 覆盖已存在

# === 推荐仓库快速安装 ===
claw skill add -i anthropics/skills                  # 官方技能库
claw skill add -i VoltAgent/awesome-openclaw-skills  # 社区精选
claw skill add -i affaan-m/everything-claude-code    # 完整配置

# === 删除 ===
claw skill remove skill-name       # 删除项目技能
claw skill remove -g skill-name    # 删除全局技能

# === 组合使用 ===
claw skill add -i -g user/repo     # 交互式全局安装
claw skill add --claude --name my user/repo # Claude + 自定义名称
```

---

## 核心价值

1. **官方支持**：Anthropic 官方仓库保证质量
2. **社区活跃**：多个高星仓库和活跃市场
3. **易于发现**：SKILLS.pub + GitHub 搜索
4. **灵活安装**：交互式、自定义名称、多位置
5. **易于分享**：基于 GitHub 的开放生态

---

**记住**：技能是 Claude/Agent 的核心扩展机制，善用官方和社区资源可以大幅提升 AI 能力！

## 快速开始

```bash
# 1. 安装官方技能（推荐）
claw skill add -i anthropics/skills

# 2. 安装社区精选
claw skill add -i VoltAgent/awesome-openclaw-skills

# 3. 浏览技能市场
# 访问 https://skills.pub/zh

# 4. 查看已安装技能
claw skill list
```
