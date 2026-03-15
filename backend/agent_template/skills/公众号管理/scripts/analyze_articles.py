#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
公众号文章数据收集脚本
收集文章的元数据用于生成分析报告
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# 配置
BASE_DIR = "高质样例/公众号"
OUTPUT_FILE = "高质样例/公众号/_系统/文章统计数据.json"

def extract_date_from_filename(filename):
    """从文件名提取日期"""
    match = re.match(r'(\d{8})', filename)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, '%Y%m%d')
        except:
            return None
    return None


def extract_title_from_filename(filename):
    """从文件名提取标题"""
    # 移除日期前缀和.md后缀
    title = re.sub(r'^\d{8}-', '', filename)
    title = re.sub(r'\.md$', '', title)
    return title


def count_words(content):
    """统计字数(中文字符)"""
    # 移除markdown标记
    content = re.sub(r'[#*`\[\]()]', '', content)
    # 统计中文字符
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', content)
    return len(chinese_chars)


def analyze_title(title):
    """分析标题特征"""
    features = {
        'length': len(title),
        'has_number': bool(re.search(r'\d+', title)),
        'has_question': '?' in title or '？' in title,
        'has_exclamation': '!' in title or '！' in title,
        'has_separator': ',' in title or '，' in title or '、' in title
    }
    return features


def collect_article_data(category, account_name, filepath):
    """收集单篇文章的数据"""
    filename = filepath.name

    # 提取日期和标题
    date = extract_date_from_filename(filename)
    title = extract_title_from_filename(filename)

    # 读取文章内容
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return None

    # 统计字数
    word_count = count_words(content)

    # 分析标题
    title_features = analyze_title(title)

    return {
        'category': category,
        'account': account_name,
        'title': title,
        'filename': filename,
        'date': date.strftime('%Y-%m-%d') if date else None,
        'word_count': word_count,
        'title_length': title_features['length'],
        'has_number': title_features['has_number'],
        'has_question': title_features['has_question'],
        'has_exclamation': title_features['has_exclamation'],
        'has_separator': title_features['has_separator']
    }


def main():
    """主函数"""
    print("📊 开始收集文章数据...")
    print("━" * 50)

    all_articles = []
    stats = {
        'total_articles': 0,
        'by_category': defaultdict(int),
        'by_account': defaultdict(int)
    }

    base_path = Path(BASE_DIR)

    # 遍历AI和写作两个分类
    for category in ['AI', '写作']:
        category_dir = base_path / category
        if not category_dir.exists():
            continue

        print(f"\n【{category}分类】")

        # 遍历每个账号
        for account_dir in category_dir.iterdir():
            if not account_dir.is_dir() or account_dir.name.startswith('_'):
                continue

            account_name = account_dir.name
            article_count = 0

            # 遍历该账号的所有文章
            for md_file in account_dir.glob('*.md'):
                article_data = collect_article_data(category, account_name, md_file)
                if article_data:
                    all_articles.append(article_data)
                    article_count += 1
                    stats['total_articles'] += 1
                    stats['by_category'][category] += 1
                    stats['by_account'][account_name] += 1

            if article_count > 0:
                print(f"  {account_name}: {article_count} 篇")

    print("\n" + "━" * 50)
    print(f"✅ 数据收集完成！")
    print(f"📊 总文章数: {stats['total_articles']} 篇")
    print(f"📁 AI分类: {stats['by_category']['AI']} 篇")
    print(f"📁 写作分类: {stats['by_category']['写作']} 篇")

    # 保存数据
    output_data = {
        'generated_at': datetime.now().isoformat(),
        'stats': dict(stats),
        'articles': all_articles
    }

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 数据已保存到: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
