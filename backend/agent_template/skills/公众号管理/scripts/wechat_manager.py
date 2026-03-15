#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号管理工具 - 统一的下载、追更、清理功能
使用方法:
  python3 wechat_manager.py sync          # 追更所有关注的账号
  python3 wechat_manager.py download 账号名  # 下载指定账号
  python3 wechat_manager.py clean         # 清理广告文章
  python3 wechat_manager.py status        # 查看状态
"""

import os
import re
import json
import time
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

# ============ 配置 ============
# 获取脚本所在目录
SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / ".wechat_api_config"
FOLLOW_FILE = "高质样例/公众号/_系统/关注列表.md"
RECORD_FILE = "高质样例/公众号/_系统/下载记录.json"
BASE_DIR = "高质样例/公众号"
MAX_ARTICLES = 20  # 根据最新接口文档限制，最大不得超过20
API_BASE = "https://down.mptext.top/api/public/v1"

# 广告关键词
AD_KEYWORDS_TITLE = [
    '链接', '购买', '商城', '福利', '课程', '联系', '微信',
    '扫码', '报名', '优惠', '特价', '秒杀', '抢购',
    '加绒', '羽绒服', '老爹鞋', '护膝', '秋裤', '袜',
    '一诺集商城', '变态', '速热', '供暖衣'
]

AD_KEYWORDS_CONTENT = [
    '感兴趣可以联系', '添加微信', '扫码关注', '课程链接',
    '限时优惠', '立即购买', '点击购买', '商品链接',
    '备注', '免费听课', '公开课', '分享会'
]


# ============ 工具函数 ============

def load_api_key():
    """加载API密钥"""
    if not CONFIG_FILE.exists():
        return None

    with open(CONFIG_FILE, 'r') as f:
        for line in f:
            if line.startswith('API_KEY='):
                return line.split('=')[1].strip().strip('"')
    return None


def check_api_key_expiry():
    """检查API密钥是否过期(4天)"""
    if not CONFIG_FILE.exists():
        return True, "配置文件不存在"

    mtime = CONFIG_FILE.stat().st_mtime
    days_old = (time.time() - mtime) / 86400

    if days_old > 4:
        return True, f"密钥已过期 {int(days_old)} 天"
    else:
        return False, f"密钥有效,还剩 {int(4 - days_old)} 天"


def load_follow_list():
    """从关注列表加载所有公众号(AI和写作分类)"""
    accounts = {'AI': [], '写作': []}

    if not os.path.exists(FOLLOW_FILE):
        return accounts

    with open(FOLLOW_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    current_category = None
    for line in content.split('\n'):
        if '## AI' in line:
            current_category = 'AI'
        elif '## 写作' in line:
            current_category = '写作'
        elif line.startswith('## '):
            current_category = None
        elif current_category and line.startswith('- '):
            accounts[current_category].append(line[2:].strip())

    return accounts


def safe_filename(title):
    """生成安全的文件名"""
    safe = re.sub(r'[\\/:*?"<>|]', '', title)
    safe = safe.strip()[:50]
    return safe


# ============ API 请求函数 ============

def api_request(url, api_key=None):
    """发送API请求"""
    import ssl
    import urllib.error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    if api_key:
        headers['X-Auth-Key'] = api_key

    req = urllib.request.Request(url, headers=headers)
    max_retries = 3
    for i in range(max_retries):
        try:
            # 创建不验证证书的SSL上下文
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(req, timeout=15, context=context) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except (urllib.error.URLError, TimeoutError, ConnectionResetError) as e:
            if i < max_retries - 1:
                print(f"  ⚠️  接口请求超时，准备重试 ({i+1}/{max_retries})...")
                time.sleep(2)
            else:
                print(f"  ❌  接口请求失败: {e}")
                return None
        except Exception as e:
            if i < max_retries - 1:
                print(f"  ⚠️  接口请求异常，准备重试 ({i+1}/{max_retries})...")
                time.sleep(2)
            else:
                print(f"  ❌  接口请求失败: {e}")
                return None


def search_account(name, api_key):
    """搜索公众号,获取fakeid"""
    encoded = urllib.parse.quote(name)
    url = f"{API_BASE}/account?keyword={encoded}&begin=0&size=1"
    data = api_request(url, api_key)

    if data and data.get('list'):
        return data['list'][0].get('fakeid')
    return None


def get_articles(fakeid, api_key, max_count=MAX_ARTICLES):
    """获取文章列表"""
    # 接口限制size最大不能超过20
    max_count = min(max_count, 20)
    url = f"{API_BASE}/article?fakeid={fakeid}&begin=0&size={max_count}"
    data = api_request(url, api_key)

    if data and data.get('articles'):
        return data['articles']
    return []


def search_account_by_url(article_url, api_key):
    """根据文章链接查询公众号"""
    encoded_url = urllib.parse.quote(article_url, safe='')
    url = f"{API_BASE}/accountbyurl?url={encoded_url}"
    data = api_request(url, api_key)
    return data


def get_author_info(fakeid):
    """查询公众号主体信息 (beta)"""
    # 此接口不需要 API 密钥
    url = f"https://down.mptext.top/api/public/beta/authorinfo?fakeid={fakeid}"
    data = api_request(url)
    return data


def get_about_biz(fakeid, key=None):
    """查询公众号主体信息(biz) (beta)"""
    # 此接口不需要 API 密钥
    url = f"https://down.mptext.top/api/public/beta/aboutbiz?fakeid={fakeid}"
    if key:
        encoded_key = urllib.parse.quote(key)
        url += f"&key={encoded_key}"
    data = api_request(url)
    return data


def download_article(link):
    """下载文章内容"""
    import ssl
    import urllib.error
    encoded_url = urllib.parse.quote(link, safe='')
    url = f"{API_BASE}/download?url={encoded_url}&format=markdown"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    
    # 重试机制
    max_retries = 3
    for i in range(max_retries):
        try:
            context = ssl._create_unverified_context()
            # 设置较短超时时间，利用重试来保证稳定性
            with urllib.request.urlopen(req, timeout=15, context=context) as resp:
                return resp.read().decode('utf-8')
        except (urllib.error.URLError, TimeoutError, ConnectionResetError) as e:
            if i < max_retries - 1:
                print(f"    ⚠️  网络超时，准备重试 ({i+1}/{max_retries})...")
                time.sleep(3)
            else:
                print(f"    ❌  下载失败 (网络异常): {e}")
                return None
        except Exception as e:
            if i < max_retries - 1:
                print(f"    ⚠️  发生异常，准备重试 ({i+1}/{max_retries})...")
                time.sleep(3)
            else:
                print(f"    ❌  下载失败 (未知异常): {e}")
                return None


# ============ 清理功能 ============

def is_ad_by_title(filename):
    """根据文件名判断是否为广告"""
    for keyword in AD_KEYWORDS_TITLE:
        if keyword in filename:
            return True
    return False


def is_ad_by_content(filepath):
    """根据内容判断是否为广告"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查文件大小
        if len(content) < 1000:
            return True, "文件太小"

        # 检查广告关键词
        ad_count = sum(1 for keyword in AD_KEYWORDS_CONTENT if keyword in content)
        if ad_count >= 2:
            return True, f"包含{ad_count}个广告关键词"

        # 检查推广内容
        if '联系' in content and ('微信' in content or '课程' in content):
            return True, "推广内容"

        return False, ""
    except Exception as e:
        return False, ""


# ============ 核心功能 ============

def download_account_articles(account_name, category, api_key):
    """下载指定公众号的文章"""
    print(f"🔍 搜索公众号: {account_name}")

    # 搜索公众号
    fakeid = search_account(account_name, api_key)
    if not fakeid:
        print("  ❌ 未找到公众号")
        return 0, 0

    print(f"  ✅ 找到公众号")

    # 创建输出目录
    output_dir = os.path.join(BASE_DIR, category, account_name)
    os.makedirs(output_dir, exist_ok=True)

    # 获取已有文件
    existing_files = set(os.listdir(output_dir)) if os.path.exists(output_dir) else set()

    # 获取文章列表前稍微等下，防止并发超限
    time.sleep(2)
    # 获取文章列表
    articles = get_articles(fakeid, api_key)
    if not articles:
        print("  ⏭️  无文章或获取失败")
        return 0, 0

    print(f"  📥 开始下载最新 {len(articles)} 篇文章...")

    downloaded = 0
    skipped = 0

    for article in articles:
        title = article.get('title', '')
        link = article.get('link', '')
        timestamp = article.get('update_time', 0)

        # 格式化日期和文件名
        date_str = datetime.fromtimestamp(timestamp).strftime('%Y%m%d')
        safe_title = safe_filename(title)
        filename = f"{date_str}-{safe_title}.md"
        filepath = os.path.join(output_dir, filename)

        # 去重检查
        if os.path.exists(filepath):
            skipped += 1
            continue

        # 检查标题重复
        if any(safe_title in f for f in existing_files):
            skipped += 1
            continue

        # 下载文章
        content = download_article(link)
        if content and len(content) > 500:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            downloaded += 1
            existing_files.add(filename)
            print(f"    ⬇️  {title[:40]}...")

        # 防止触发限制，拉长请求间距
        time.sleep(3)

    return downloaded, skipped


def cmd_sync(api_key):
    """追更所有关注的公众号"""
    print("📡 公众号追更开始...")
    print("━" * 50)

    accounts = load_follow_list()
    total_accounts = sum(len(v) for v in accounts.values())

    if total_accounts == 0:
        print("❌ 没有找到关注的账号")
        return

    print(f"📋 共 {total_accounts} 个账号待检查\n")

    total_new = 0
    total_skip = 0
    updated_accounts = []

    for category, account_list in accounts.items():
        if not account_list:
            continue

        print(f"\n【{category}分类】")
        for account in account_list:
            print(f"  {account}")
            try:
                downloaded, skipped = download_account_articles(account, category, api_key)
                if downloaded > 0:
                    print(f"    ✅ 新增 {downloaded} 篇")
                    total_new += downloaded
                    updated_accounts.append(f"{category}/{account}")
                else:
                    print(f"    ⏭️  无新文章")
                total_skip += skipped
            except Exception as e:
                print(f"    ❌ 账号 {account} 抓取异常: {e}")
                continue

    print("\n" + "━" * 50)
    print("🎉 追更完成！")
    print(f"📊 新增: {total_new} 篇")
    print(f"⏭️  跳过: {total_skip} 篇")
    if updated_accounts:
        print(f"📝 有更新: {', '.join(updated_accounts)}")


def cmd_download(account_name, api_key):
    """下载指定公众号"""
    print("📥 下载指定公众号...")
    print("━" * 50)

    # 从关注列表查找分类
    accounts = load_follow_list()
    category = None

    for cat, account_list in accounts.items():
        if account_name in account_list:
            category = cat
            break

    if not category:
        print(f"⚠️  '{account_name}' 不在关注列表中")
        print("请选择分类: AI 或 写作")
        category = input("分类: ").strip()
        if category not in ['AI', '写作']:
            print("❌ 分类必须是 'AI' 或 '写作'")
            return

    print(f"分类: {category}\n")

    downloaded, skipped = download_account_articles(account_name, category, api_key)

    print("\n" + "━" * 50)
    print("🎉 下载完成！")
    print(f"📊 新下载: {downloaded} 篇")
    print(f"⏭️  跳过: {skipped} 篇")
    print(f"📁 保存位置: {BASE_DIR}/{category}/{account_name}")


def cmd_clean():
    """清理广告和无效文章"""
    print("🧹 开始清理文章...")
    print("━" * 50)

    deleted_files = []
    kept_files = []

    # 遍历AI和写作两个分类
    for category in ['AI', '写作']:
        category_dir = Path(BASE_DIR) / category
        if not category_dir.exists():
            continue

        print(f"\n【{category}分类】")

        for md_file in category_dir.rglob('*.md'):
            # 跳过系统文件
            if '_系统' in str(md_file):
                continue

            filename = md_file.name

            # 检查标题
            if is_ad_by_title(filename):
                print(f"  🗑️  删除(标题广告): {md_file.relative_to(category_dir)}")
                deleted_files.append((str(md_file.relative_to(category_dir)), "标题广告"))
                md_file.unlink()
                continue

            # 检查内容
            is_ad, reason = is_ad_by_content(md_file)
            if is_ad:
                print(f"  🗑️  删除({reason}): {md_file.relative_to(category_dir)}")
                deleted_files.append((str(md_file.relative_to(category_dir)), reason))
                md_file.unlink()
            else:
                kept_files.append(str(md_file.relative_to(category_dir)))

    print("\n" + "━" * 50)
    print("🎉 清理完成！")
    print(f"🗑️  删除: {len(deleted_files)} 篇")
    print(f"✅ 保留: {len(kept_files)} 篇")


def cmd_status():
    """查看系统状态"""
    print("📊 系统状态")
    print("━" * 50)

    # API密钥状态
    expired, msg = check_api_key_expiry()
    if expired:
        print(f"❌ API密钥: {msg}")
        print("   请访问 https://down.mptext.top 获取新密钥")
    else:
        print(f"✅ API密钥: {msg}")

    # 关注列表
    accounts = load_follow_list()
    print(f"\n📋 关注列表:")
    for category, account_list in accounts.items():
        print(f"  {category}: {len(account_list)} 个账号")
        for account in account_list:
            print(f"    - {account}")

    # 文章统计
    print(f"\n📁 文章统计:")
    for category in ['AI', '写作']:
        category_dir = Path(BASE_DIR) / category
        if category_dir.exists():
            count = len(list(category_dir.rglob('*.md')))
            print(f"  {category}: {count} 篇")

    print("━" * 50)


# ============ 主函数 ============

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("公众号管理工具")
        print("\n使用方法:")
        print("  python3 wechat_manager.py sync              # 追更所有关注的账号")
        print("  python3 wechat_manager.py download 账号名    # 下载指定账号")
        print("  python3 wechat_manager.py clean             # 清理广告文章")
        print("  python3 wechat_manager.py status            # 查看状态")
        return

    command = sys.argv[1]

    # 状态命令不需要API密钥
    if command == 'status':
        cmd_status()
        return

    # 清理命令不需要API密钥
    if command == 'clean':
        cmd_clean()
        return

    # 其他命令需要API密钥
    api_key = load_api_key()
    if not api_key:
        print("❌ API密钥未配置")
        print(f"请在 {CONFIG_FILE} 中配置 API_KEY")
        print("获取密钥: https://down.mptext.top")
        return

    # 检查密钥是否过期
    expired, msg = check_api_key_expiry()
    if expired:
        print(f"⚠️  {msg}")
        print("请访问 https://down.mptext.top 获取新密钥")
        print()

    if command == 'sync':
        cmd_sync(api_key)
    elif command == 'download':
        if len(sys.argv) < 3:
            print("❌ 请指定公众号名称")
            print("使用方法: python3 wechat_manager.py download 账号名")
            return
        account_name = sys.argv[2]
        cmd_download(account_name, api_key)
    else:
        print(f"❌ 未知命令: {command}")
        print("可用命令: sync, download, clean, status")


if __name__ == "__main__":
    main()
