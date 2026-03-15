#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
清理公众号文章：删除广告和下载失败的文件
"""

import os
import re
from pathlib import Path

# 广告关键词（标题中出现这些词的文章会被删除）
AD_KEYWORDS_TITLE = [
    '链接', '购买', '商城', '福利', '课程', '联系', '微信',
    '扫码', '报名', '优惠', '特价', '秒杀', '抢购',
    '加绒', '羽绒服', '老爹鞋', '护膝', '秋裤', '袜',
    '一诺集商城', '变态', '速热', '供暖衣'
]

# 内容中的广告关键词（需要检查文章内容）
AD_KEYWORDS_CONTENT = [
    '感兴趣可以联系', '添加微信', '扫码关注', '课程链接',
    '限时优惠', '立即购买', '点击购买', '商品链接',
    '备注', '免费听课', '公开课', '分享会'
]

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
            
        # 检查文件大小（字节）
        if len(content) < 1000:  # 小于1KB
            return True, "文件太小"
            
        # 检查是否包含大量广告关键词
        ad_count = sum(1 for keyword in AD_KEYWORDS_CONTENT if keyword in content)
        if ad_count >= 2:
            return True, f"包含{ad_count}个广告关键词"
            
        # 检查是否主要是推广内容（链接、联系方式等）
        if '联系' in content and ('微信' in content or '课程' in content):
            return True, "推广内容"
            
        return False, ""
    except Exception as e:
        print(f"  ⚠️  读取文件出错: {filepath} - {e}")
        return False, ""

def clean_articles(base_dir):
    """清理文章"""
    base_path = Path(base_dir)
    
    deleted_files = []
    kept_files = []
    
    # 遍历所有 markdown 文件
    for md_file in base_path.rglob('*.md'):
        filename = md_file.name
        
        # 检查标题
        if is_ad_by_title(filename):
            print(f"🗑️  删除（标题广告）: {md_file.relative_to(base_path)}")
            deleted_files.append((str(md_file.relative_to(base_path)), "标题广告"))
            md_file.unlink()
            continue
        
        # 检查内容
        is_ad, reason = is_ad_by_content(md_file)
        if is_ad:
            print(f"🗑️  删除（{reason}）: {md_file.relative_to(base_path)}")
            deleted_files.append((str(md_file.relative_to(base_path)), reason))
            md_file.unlink()
        else:
            kept_files.append(str(md_file.relative_to(base_path)))
    
    return deleted_files, kept_files

if __name__ == '__main__':
    base_dir = '高质样例/公众号/写作'
    
    print("🔍 开始清理文章...")
    print(f"📁 目标目录: {base_dir}\n")
    
    deleted, kept = clean_articles(base_dir)
    
    print(f"\n✅ 清理完成！")
    print(f"🗑️  删除: {len(deleted)} 篇")
    print(f"✅ 保留: {len(kept)} 篇")
    
    if deleted:
        print(f"\n删除的文件列表：")
        for filepath, reason in deleted:
            print(f"  - {filepath} ({reason})")
