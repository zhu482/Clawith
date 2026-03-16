#!/bin/bash

# 批量下载微信公众号文章到知识库
# 使用方法: ./batch_download_wechat.sh "分类" "公众号名称"
# 分类: AI 或 写作

CATEGORY="$1"
ACCOUNT_NAME="$2"
MAX_ARTICLES=30

# 读取配置文件中的 API 密钥
CONFIG_FILE=".wechat_api_config"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ 配置文件不存在: $CONFIG_FILE"
    echo "请先创建配置文件并填入 API 密钥"
    exit 1
fi

# 加载配置
source "$CONFIG_FILE"

if [ -z "$CATEGORY" ] || [ -z "$ACCOUNT_NAME" ]; then
    echo "使用方法: $0 \"分类\" \"公众号名称\""
    echo ""
    echo "分类选项:"
    echo "  AI    - AI相关公众号"
    echo "  写作  - 写作相关公众号"
    echo ""
    echo "示例:"
    echo "  $0 \"写作\" \"卡兹克\""
    echo "  $0 \"AI\" \"机器之心\""
    exit 1
fi

# 验证分类
if [ "$CATEGORY" != "AI" ] && [ "$CATEGORY" != "写作" ]; then
    echo "❌ 分类必须是 'AI' 或 '写作'"
    exit 1
fi

OUTPUT_DIR="高质样例/公众号/${CATEGORY}/${ACCOUNT_NAME}"

if [ -z "$API_KEY" ]; then
    echo "❌ API 密钥未配置，请检查 $CONFIG_FILE"
    exit 1
fi

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

echo "🔍 正在搜索公众号: $ACCOUNT_NAME"

# URL 编码公众号名称
ENCODED_NAME=$(python3 -c "import urllib.parse; print(urllib.parse.quote('${ACCOUNT_NAME}'))")

# 1. 搜索公众号，获取 fakeid
SEARCH_RESULT=$(curl -s "https://down.mptext.top/api/public/v1/account?keyword=${ENCODED_NAME}&begin=0&size=1" \
  -H "X-Auth-Key: ${API_KEY}")

FAKEID=$(echo "$SEARCH_RESULT" | grep -o '"fakeid":"[^"]*"' | head -1 | cut -d'"' -f4)

if [ -z "$FAKEID" ]; then
    echo "❌ 未找到公众号: $ACCOUNT_NAME"
    exit 1
fi

echo "✅ 找到公众号，ID: $FAKEID"
echo "📥 开始下载最新 ${MAX_ARTICLES} 篇文章..."

# 2. 获取文章列表（最新30篇）
ARTICLES=$(curl -s "https://down.mptext.top/api/public/v1/article?fakeid=${FAKEID}&begin=0&size=20" \
  -H "X-Auth-Key: ${API_KEY}")

# 保存到临时文件以便解析
TEMP_FILE=$(mktemp)
echo "$ARTICLES" > "$TEMP_FILE"

TOTAL_DOWNLOADED=0
SKIPPED=0

# 使用 Python 解析 JSON 并下载（更可靠）
python3 - <<EOF
import json
import urllib.parse
import subprocess
import os
import re
from datetime import datetime

with open('$TEMP_FILE', 'r') as f:
    data = json.load(f)

# 直接从 articles 数组获取文章
articles = data.get('articles', [])[:$MAX_ARTICLES]

downloaded = 0
skipped = 0

for article in articles:
    title = article.get('title', '')
    link = article.get('link', '')
    timestamp = article.get('update_time', 0)
    
    # 格式化日期
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y%m%d')
    
    # 清理文件名（移除特殊字符）
    safe_title = re.sub(r'[\\/:*?"<>|]', '', title)
    safe_title = safe_title.strip()[:50]  # 限制长度
    
    filename = f"$OUTPUT_DIR/{date_str}-{safe_title}.md"
    
    # 去重：检查文件是否已存在
    if os.path.exists(filename):
        print(f"  ⏭️  跳过（已存在）: {title}")
        skipped += 1
        continue
    
    # 检查是否有相同标题的文件（不同日期）
    if os.path.exists('$OUTPUT_DIR'):
        existing_files = [f for f in os.listdir('$OUTPUT_DIR') if safe_title in f]
        if existing_files:
            print(f"  ⏭️  跳过（标题重复）: {title}")
            skipped += 1
            continue
    
    print(f"  ⬇️  下载: {title}")
    
    # 下载文章
    encoded_url = urllib.parse.quote(link, safe='')
    download_url = f"https://down.mptext.top/api/public/v1/download?url={encoded_url}&format=markdown"
    
    result = subprocess.run(
        ['curl', '-s', download_url, '-o', filename],
        capture_output=True
    )
    
    if result.returncode == 0:
        downloaded += 1
    
    # 避免请求过快
    subprocess.run(['sleep', '1'])

print(f"\n🎉 下载完成！")
print(f"📊 新下载: {downloaded} 篇")
print(f"⏭️  跳过: {skipped} 篇")
print(f"📁 保存位置: $OUTPUT_DIR")
EOF

# 清理临时文件
rm -f "$TEMP_FILE"
