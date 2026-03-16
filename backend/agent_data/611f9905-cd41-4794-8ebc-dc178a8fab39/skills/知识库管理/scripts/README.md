# 个人写作知识库

基于 Git + 本地向量库的个人写作系统

## 目录结构

- `创作空间/` - 创作内容
- `高质样例/` - 学习素材
- `个人信息及记忆/` - 个人画像和记忆
- `写作方法/` - 写作方法库

## 快速开始

### 首次使用

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 初始化向量库（5分钟）
python init_vector_db.py
```

### 日常使用

```bash
# 1. 拉取最新内容
git pull

# 2. 更新向量库（几秒钟）
python update_vector_db.py
```

### 下载公众号文章

```bash
python .agent/skills/05-内容工具/公众号管理/scripts/sync_wechat.py
```

## 跨设备使用

### 在新电脑上

```bash
# 1. 克隆仓库
git clone <你的仓库地址>

# 2. 安装依赖
pip install -r requirements.txt

# 3. 初始化向量库
python init_vector_db.py
```

### 同步更新

```bash
git pull && python update_vector_db.py
```

## 注意事项

- 向量库数据（`.vector_db/`）不会同步到 Git
- 每台电脑需要独立建索引（自动化，很快）
- 私密配置文件已加入 `.gitignore`
