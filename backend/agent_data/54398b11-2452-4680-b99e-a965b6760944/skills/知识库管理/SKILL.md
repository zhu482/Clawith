---
name: vector-manager
description: 知识库索引系统。管理向量库的初始化、更新、检索，为公众号文章内容提供语义搜索能力。
trigger_keywords: [向量库, 更新向量库, 知识库管理, 索引文档, 向量化]
version: 1.0.0
---

# 向量库管理 - 知识库索引系统

向量库是知识库的索引系统，用于快速检索公众号文章内容。

## 为什么需要向量库？

向量库把文章内容转换成数学向量，让AI能快速找到相关内容。就像给知识库建了个搜索引擎。

**核心价值**：
- 快速检索：从几百篇文章中秒级找到相关内容
- 语义理解：不是简单的关键词匹配，而是理解意思
- 自动更新：新下载的文章自动加入索引

## 向量库的工作流程

```
公众号文章 → 向量化 → 存储到.vector_db → 检索使用
```

**技术栈**：
- `sentence_transformers`：把文本转换成向量
- `pickle`：存储向量数据
- 模型：`paraphrase-multilingual-MiniLM-L12-v2`（支持中文）

---

## AI的向量库技能

## 使用方法

### 1. 初始化向量库（首次使用）

**触发场景**：
- 新电脑首次使用
- 向量库文件损坏或丢失
- 用户明确要求重建向量库

**执行命令**：
```bash
.venv/bin/python3 .agent/skills/00-系统核心/知识库管理/scripts/init_vector_db.py
```

**说明**：
- 会扫描 `高质样例/公众号/` 下所有文章
- 每篇文章按1000字分块
- 生成向量并保存到 `.vector_db/articles.pkl`
- 首次运行需要几分钟

---

### 2. 更新向量库（增量更新）

**触发场景**：
- 用户下载了新的公众号文章
- 用户说"更新向量库"、"同步向量库"
- 追更后自动触发

**执行步骤**：

**第一步：检查是否有新文章**
```bash
.venv/bin/python3 -c "
import pickle
import os

# 加载现有向量库
with open('.vector_db/articles.pkl', 'rb') as f:
    data = pickle.load(f)

indexed_files = set(a['file_path'] for a in data['articles'])

# 检查新文章
new_files = []
for root, dirs, files in os.walk('高质样例/公众号'):
    if '_系统' in root:
        continue
    for file in files:
        if file.endswith('.md') and not file.startswith('_'):
            filepath = os.path.join(root, file)
            if filepath not in indexed_files:
                new_files.append(filepath)

print(f'发现 {len(new_files)} 个新文章')
"
```

**第二步：更新向量库**
```bash
.venv/bin/python3 .agent/skills/00-系统核心/知识库管理/scripts/update_vector_db.py
```

**说明**：
- 只处理新增的文章，不重复索引
- 自动合并到现有向量库
- 更新后文件大小会增加

---

### 3. 提交到远程git

**触发场景**：
- 向量库更新后
- 用户说"上传向量库"、"提交到git"

**执行步骤**：

```bash
# 1. 强制添加向量库文件（.gitignore会忽略它）
git add -f .vector_db/articles.pkl

# 2. 添加新下载的公众号文章
git add 高质样例/公众号/

# 3. 提交
git commit -m "更新向量库：新增XX篇公众号文章（日期）"

# 4. 推送到远程
git push
```

**注意**：
- 向量库文件被 `.gitignore` 忽略，需要用 `-f` 强制添加
- 提交信息要说明新增了多少篇文章
- 确保公众号文章和向量库一起提交

---

### 4. 检索向量库

**触发场景**：
- 用户要求检索（参考"技能_检索.md"）
- 选题深化时需要补充素材
- 写作时需要找相关案例

**执行命令**：
```bash
.venv/bin/python3 .agent/skills/00-系统核心/知识库管理/scripts/search_articles.py "关键词"
```

**说明**：
- 会返回最相关的5篇文章
- 包含文章路径、标题、相关度评分
- 结果记录到 `00_素材索引.md`

---

## 常见问题

### Q1: 向量库文件多大？
- 初始约10-15MB
- 每次更新增加几MB
- 不会无限增长（有压缩）

### Q2: 更新向量库需要多久？
- 取决于新文章数量
- 约50篇文章需要5-10秒
- 会显示进度条

### Q3: 向量库损坏怎么办？
- 删除 `.vector_db/articles.pkl`
- 重新运行 `.agent/skills/00-系统核心/知识库管理/scripts/init_vector_db.py`
- 重新索引所有文章

### Q4: 为什么要提交到git？
- 多设备同步（家里电脑、公司电脑）
- 备份（防止丢失）
- 版本管理（可以回退）

### Q5: 虚拟环境损坏怎么办？

**症状**：
- 运行脚本时提示 `ModuleNotFoundError: No module named 'numpy'`
- 或者提示 `zsh: command not found: python`
- 或者 `.venv/bin/python` 文件损坏

**解决方法**：

```bash
# 1. 删除旧的虚拟环境
rm -rf .venv

# 2. 重新创建虚拟环境
python3 -m venv .venv

# 3. 安装依赖
source .venv/bin/activate && pip install -r .agent/skills/00-系统核心/知识库管理/scripts/requirements.txt

# 4. 测试是否修复
source .venv/bin/activate && python .agent/skills/00-系统核心/知识库管理/scripts/update_vector_db.py
```

**快速命令**（一键修复）：
```bash
rm -rf .venv && python3 -m venv .venv && source .venv/bin/activate && pip install -r .agent/skills/00-系统核心/知识库管理/scripts/requirements.txt
```

---

## 文件位置

```
工作目录/
├── .vector_db/
│   └── articles.pkl          # 向量库文件
├── scripts/
│   └── vector/
│       ├── init_vector_db.py         # 初始化脚本
│       ├── update_vector_db.py       # 更新脚本
│       └── search_articles.py        # 检索脚本
└── 高质样例/公众号/          # 文章来源
```

## 核心原则

1. **自动化优先** - 追更后自动更新向量库
2. **增量更新** - 只处理新文章，不重复索引
3. **及时提交** - 更新后立即提交到git
4. **保持同步** - 向量库和文章一起管理

---

**记住**：向量库是知识库的索引，不是知识库本身。文章才是核心，向量库只是让检索更快。
