#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号追更脚本
只追更AI分类的公众号，增量下载新文章
使用方法: python3 sync_wechat.py
"""

import os
import re
import json
import time
import urllib.parse
import urllib.request
import ssl
from datetime import datetime

# 配置
CONFIG_FILE = ".wechat_api_config"
RECORD_FILE = "高质样例/公众号/_系统/下载记录.json"
FOLLOW_FILE = "高质样例/公众号/_系统/关注列表.md"
BASE_DIR = "高质样例/公众号/AI"
MAX_ARTICLES = 20
API_BASE = "https://down.mptext.top/api/public/v1"

def load_api_key():
    """加载API密钥"""
    if not os.path.exists(CONFIG_FILE):
        print(f"❌ 配置文件不存在: {CONFIG_FILE}")
        return None
    
    with open(CONFIG_FILE, 'r') as f:
        for line in f:
            if line.startswith('API_KEY='):
                return line.split('=')[1].strip().strip('"')
    return None

def load_follow_list():
    """从关注列表提取AI分类的公众号"""
    accounts = []
    if not os.path.exists(FOLLOW_FILE):
        print(f"❌ 关注列表不存在: {FOLLOW_FILE}")
        return accounts
    
    with open(FOLLOW_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取AI分类下的账号
    in_ai_section = False
    for line in content.split('\n'):
        if '## AI' in line:
            in_ai_section = True
            continue
        if line.startswith('## ') and in_ai_section:
            break
        if in_ai_section and line.startswith('- '):
            accounts.append(line[2:].strip())
    
    return accounts

def api_request(url, api_key=None):
    """发送API请求"""
    headers = {}
    if api_key:
        headers['X-Auth-Key'] = api_key
    
    # 创建SSL上下文，忽略证书验证
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  ⚠️  请求失败: {e}")
        return None

def search_account(name, api_key):
    """搜索公众号，获取fakeid"""
    encoded = urllib.parse.quote(name)
    url = f"{API_BASE}/account?keyword={encoded}&begin=0&size=1"
    data = api_request(url, api_key)
    
    if data and data.get('list'):
        return data['list'][0].get('fakeid')
    return None

def get_articles(fakeid, api_key):
    """获取文章列表"""
    # 根据最新接口要求，最大限制不能超过20
    max_count = min(MAX_ARTICLES, 20)
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
    """查询公众号主体信息 (beta) - 不需要API密钥"""
    url = f"https://down.mptext.top/api/public/beta/authorinfo?fakeid={fakeid}"
    data = api_request(url)
    return data

def get_about_biz(fakeid, key=None):
    """查询公众号主体信息(biz) (beta) - 不需要API密钥"""
    url = f"https://down.mptext.top/api/public/beta/aboutbiz?fakeid={fakeid}"
    if key:
        encoded_key = urllib.parse.quote(key)
        url += f"&key={encoded_key}"
    data = api_request(url)
    return data

def download_article(link):
    """下载文章内容"""
    encoded_url = urllib.parse.quote(link, safe='')
    url = f"{API_BASE}/download?url={encoded_url}&format=markdown"
    
    # 创建SSL上下文，忽略证书验证
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.read().decode('utf-8')
    except:
        return None

def safe_filename(title):
    """生成安全的文件名"""
    # 移除特殊字符
    safe = re.sub(r'[\\/:*?"<>|]', '', title)
    safe = safe.strip()[:50]
    return safe

def main():
    print("📡 公众号追更开始...")
    print("━" * 40)
    
    api_key = load_api_key()
    if not api_key:
        print("❌ API密钥未配置")
        return
    
    accounts = load_follow_list()
    if not accounts:
        print("❌ 没有找到关注的账号")
        return
    
    print(f"📋 共 {len(accounts)} 个账号待检查\n")
    
    total_new = 0
    total_skip = 0
    updated_accounts = []
    
    for account in accounts:
        print(f"🔍 检查: {account}")
        
        # 搜索公众号
        fakeid = search_account(account, api_key)
        if not fakeid:
            print("  ⚠️  未找到，跳过")
            continue
        
        # 创建目录
        output_dir = os.path.join(BASE_DIR, account)
        os.makedirs(output_dir, exist_ok=True)
        
        # 获取已有文件
        existing_files = set(os.listdir(output_dir)) if os.path.exists(output_dir) else set()
        
        # 获取文章列表
        articles = get_articles(fakeid, api_key)
        if not articles:
            print("  ⏭️  无文章或获取失败")
            continue
        
        downloaded = 0
        skipped = 0
        
        for article in articles:
            title = article.get('title', '')
            link = article.get('link', '')
            timestamp = article.get('update_time', 0)
            
            # 格式化日期
            date_str = datetime.fromtimestamp(timestamp).strftime('%Y%m%d')
            safe_title = safe_filename(title)
            filename = f"{date_str}-{safe_title}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 去重检查
            if os.path.exists(filepath):
                skipped += 1
                continue
            
            # 检查标题重复
            title_exists = any(safe_title in f for f in existing_files)
            if title_exists:
                skipped += 1
                continue
            
            # 下载文章
            content = download_article(link)
            if content and len(content) > 500:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                downloaded += 1
                existing_files.add(filename)
                print(f"  ⬇️  {title[:30]}...")
            
            time.sleep(0.5)  # 避免请求过快
        
        if downloaded > 0:
            print(f"  ✅ 新增 {downloaded} 篇")
            total_new += downloaded
            updated_accounts.append(account)
        else:
            print(f"  ⏭️  无新文章")
        
        total_skip += skipped
    
    # 更新下载记录
    record = {"last_sync": datetime.now().isoformat(), "accounts": {}}
    with open(RECORD_FILE, 'w', encoding='utf-8') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    
    print()
    print("━" * 40)
    print("🎉 追更完成！")
    print(f"📊 新增: {total_new} 篇")
    print(f"⏭️  跳过: {total_skip} 篇（已存在）")
    if updated_accounts:
        print(f"📝 有更新: {', '.join(updated_accounts)}")

if __name__ == "__main__":
    main()
