#!/usr/bin/env python3
"""
分析斜杠青年小冯的抖音视频数据
"""
import json
import os
from pathlib import Path
from typing import List, Dict
import re

def load_all_metadata(base_dir: str) -> List[Dict]:
    """加载所有metadata.json文件"""
    metadata_list = []
    base_path = Path(base_dir)
    
    for metadata_file in base_path.rglob("metadata.json"):
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                metadata_list.append(data)
        except Exception as e:
            print(f"Error loading {metadata_file}: {e}")
    
    return metadata_list

def extract_title_core(title: str) -> str:
    """提取标题核心部分（去掉hashtag）"""
    # 移除 # 开头的标签
    core = re.split(r'\s*#', title)[0].strip()
    return core

def analyze_data(metadata_list: List[Dict]) -> Dict:
    """分析数据"""
    # 按点赞数排序
    sorted_by_likes = sorted(metadata_list, key=lambda x: int(x.get('liked_count', 0)), reverse=True)
    
    # 按收藏数排序
    sorted_by_collects = sorted(metadata_list, key=lambda x: int(x.get('collected_count', 0)), reverse=True)
    
    # 计算总体数据
    total_videos = len(metadata_list)
    total_likes = sum(int(x.get('liked_count', 0)) for x in metadata_list)
    total_collects = sum(int(x.get('collected_count', 0)) for x in metadata_list)
    total_comments = sum(int(x.get('comment_count', 0)) for x in metadata_list)
    total_shares = sum(int(x.get('share_count', 0)) for x in metadata_list)
    
    avg_likes = total_likes / total_videos if total_videos > 0 else 0
    avg_collects = total_collects / total_videos if total_videos > 0 else 0
    
    return {
        'sorted_by_likes': sorted_by_likes,
        'sorted_by_collects': sorted_by_collects,
        'total_videos': total_videos,
        'total_likes': total_likes,
        'total_collects': total_collects,
        'total_comments': total_comments,
        'total_shares': total_shares,
        'avg_likes': avg_likes,
        'avg_collects': avg_collects,
    }

def analyze_title_patterns(metadata_list: List[Dict]) -> Dict:
    """分析标题模式"""
    patterns = {
        '数字型': [],  # 包含具体数字
        '疑问型': [],  # 如何、怎么、为什么
        '权威背书': [],  # 董事长、总监、顶级
        '时间紧迫': [],  # 一定要、尽早、20多岁
        '颠覆认知': [],  # 真相、从来不会告诉你、脱胎换骨
        '实战经验': [],  # 复盘、我的、经验
        '底层逻辑': [],  # 本质、底层、思维
    }
    
    for item in metadata_list:
        title = item.get('title', '')
        core_title = extract_title_core(title)
        
        # 数字型
        if re.search(r'\d+', core_title):
            patterns['数字型'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 疑问型
        if re.search(r'如何|怎么|为什么|吗', core_title):
            patterns['疑问型'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 权威背书
        if re.search(r'董事长|总监|顶级|聪明人|牛人|高手', core_title):
            patterns['权威背书'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 时间紧迫
        if re.search(r'一定要|尽早|20多岁|马上|立刻|现在', core_title):
            patterns['时间紧迫'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 颠覆认知
        if re.search(r'真相|从来|永远|脱胎换骨|颠覆|揭示', core_title):
            patterns['颠覆认知'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 实战经验
        if re.search(r'复盘|我的|经验|分享|教我', core_title):
            patterns['实战经验'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
        
        # 底层逻辑
        if re.search(r'本质|底层|思维|认知|逻辑', core_title):
            patterns['底层逻辑'].append({
                'title': core_title,
                'likes': int(item.get('liked_count', 0)),
                'collects': int(item.get('collected_count', 0))
            })
    
    # 对每个模式按点赞数排序
    for key in patterns:
        patterns[key] = sorted(patterns[key], key=lambda x: x['likes'], reverse=True)
    
    return patterns

def generate_report(analysis: Dict, patterns: Dict, output_file: str):
    """生成分析报告"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 斜杠青年小冯 - 抖音视频数据分析报告\n\n")
        
        # 总体数据
        f.write("## 📊 总体数据\n\n")
        f.write(f"- **视频总数**: {analysis['total_videos']}\n")
        f.write(f"- **总点赞数**: {analysis['total_likes']:,}\n")
        f.write(f"- **总收藏数**: {analysis['total_collects']:,}\n")
        f.write(f"- **总评论数**: {analysis['total_comments']:,}\n")
        f.write(f"- **总分享数**: {analysis['total_shares']:,}\n")
        f.write(f"- **平均点赞**: {analysis['avg_likes']:.0f}\n")
        f.write(f"- **平均收藏**: {analysis['avg_collects']:.0f}\n\n")
        
        # Top 20 点赞最高
        f.write("## 🔥 Top 20 点赞最高视频\n\n")
        f.write("| 排名 | 标题 | 点赞 | 收藏 | 评论 | 分享 | 收藏率 |\n")
        f.write("|------|------|------|------|------|------|--------|\n")
        
        for i, item in enumerate(analysis['sorted_by_likes'][:20], 1):
            title = extract_title_core(item.get('title', ''))
            likes = int(item.get('liked_count', 0))
            collects = int(item.get('collected_count', 0))
            comments = int(item.get('comment_count', 0))
            shares = int(item.get('share_count', 0))
            collect_rate = (collects / likes * 100) if likes > 0 else 0
            
            f.write(f"| {i} | {title[:50]}... | {likes:,} | {collects:,} | {comments} | {shares} | {collect_rate:.1f}% |\n")
        
        f.write("\n")
        
        # Top 20 收藏最高
        f.write("## 💾 Top 20 收藏最高视频\n\n")
        f.write("| 排名 | 标题 | 点赞 | 收藏 | 评论 | 分享 | 收藏率 |\n")
        f.write("|------|------|------|------|------|------|--------|\n")
        
        for i, item in enumerate(analysis['sorted_by_collects'][:20], 1):
            title = extract_title_core(item.get('title', ''))
            likes = int(item.get('liked_count', 0))
            collects = int(item.get('collected_count', 0))
            comments = int(item.get('comment_count', 0))
            shares = int(item.get('share_count', 0))
            collect_rate = (collects / likes * 100) if likes > 0 else 0
            
            f.write(f"| {i} | {title[:50]}... | {likes:,} | {collects:,} | {comments} | {shares} | {collect_rate:.1f}% |\n")
        
        f.write("\n")
        
        # 标题模式分析
        f.write("## 🎯 标题模式分析\n\n")
        
        for pattern_name, items in patterns.items():
            if items:
                f.write(f"### {pattern_name} ({len(items)}条)\n\n")
                avg_likes = sum(x['likes'] for x in items) / len(items)
                avg_collects = sum(x['collects'] for x in items) / len(items)
                f.write(f"**平均点赞**: {avg_likes:.0f} | **平均收藏**: {avg_collects:.0f}\n\n")
                
                # 显示Top 5
                f.write("**Top 5 案例**:\n\n")
                for i, item in enumerate(items[:5], 1):
                    f.write(f"{i}. {item['title']} (👍 {item['likes']:,} | 💾 {item['collects']:,})\n")
                f.write("\n")
        
        # 爆款标题特征总结
        f.write("## 💡 爆款标题特征总结\n\n")
        
        # 分析Top 10的共同特征
        top10 = analysis['sorted_by_likes'][:10]
        f.write("### Top 10 爆款标题的共同特征\n\n")
        
        for i, item in enumerate(top10, 1):
            title = extract_title_core(item.get('title', ''))
            likes = int(item.get('liked_count', 0))
            f.write(f"{i}. **{title}** (👍 {likes:,})\n")
        
        f.write("\n### 核心发现\n\n")
        f.write("1. **数字具象化**: 大量使用具体数字（20w粉、1600条、2000年前）增强可信度\n")
        f.write("2. **权威背书**: 借用\"董事长\"、\"顶级聪明人\"等权威形象建立信任\n")
        f.write("3. **认知颠覆**: \"真相\"、\"从来不会告诉你\"、\"脱胎换骨\"等词汇制造认知冲击\n")
        f.write("4. **实战导向**: \"复盘\"、\"我的经验\"、\"教我\"等强调实战价值\n")
        f.write("5. **紧迫感**: \"一定要\"、\"20多岁\"等制造时间紧迫感\n")
        f.write("6. **底层思维**: 强调\"本质\"、\"底层\"、\"思维\"等深层认知\n")
        f.write("7. **财富主题**: 大量涉及赚钱、财富、创业等高关注话题\n\n")

def main():
    base_dir = "/Users/zhuzhiheng/Desktop/文章/视频资源/douyin/斜杠青年小冯"
    output_file = "/Users/zhuzhiheng/Desktop/文章/创作空间/斜杠青年小冯_数据分析报告.md"
    
    print("正在加载数据...")
    metadata_list = load_all_metadata(base_dir)
    print(f"已加载 {len(metadata_list)} 条视频数据")
    
    print("正在分析数据...")
    analysis = analyze_data(metadata_list)
    
    print("正在分析标题模式...")
    patterns = analyze_title_patterns(metadata_list)
    
    print("正在生成报告...")
    generate_report(analysis, patterns, output_file)
    
    print(f"✅ 报告已生成: {output_file}")

if __name__ == "__main__":
    main()
