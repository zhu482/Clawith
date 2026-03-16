import json
from datetime import datetime
from collections import Counter
import re

def analyze_creator_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data:
        return "No data found."

    total_videos = len(data)
    likes = []
    collects = []
    comments = []
    shares = []
    dates = []
    hashtags = []
    titles = []

    for item in data:
        likes.append(int(item.get('liked_count', 0)))
        collects.append(int(item.get('collected_count', 0)))
        comments.append(int(item.get('comment_count', 0)))
        shares.append(int(item.get('share_count', 0)))
        
        ts = item.get('create_time')
        if ts:
            dates.append(datetime.fromtimestamp(ts))
        
        title = item.get('title', '')
        titles.append(title)
        
        # 提取 hashtag
        tags = re.findall(r'#(\w+)', title)
        hashtags.extend(tags)

    # 统计数据
    avg_likes = sum(likes) / total_videos
    avg_collects = sum(collects) / total_videos
    avg_comments = sum(comments) / total_videos
    avg_shares = sum(shares) / total_videos
    
    dates.sort()
    start_date = dates[0].strftime('%Y-%m-%d')
    end_date = dates[-1].strftime('%Y-%m-%d')
    
    top_hashtags = Counter(hashtags).most_common(10)
    
    # 打印结果供 AI 参考
    print(f"Total Videos: {total_videos}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Avg Likes: {avg_likes:.2f}")
    print(f"Avg Collects: {avg_collects:.2f}")
    print(f"Avg Comments: {avg_comments:.2f}")
    print(f"Avg Shares: {avg_shares:.2f}")
    print(f"Top 10 Hashtags: {top_hashtags}")
    
    # 抽取 10 个典型标题分析风格
    print("\nSample Titles:")
    for t in titles[:10]:
        print(f"- {t}")

if __name__ == "__main__":
    analyze_creator_data('/Users/zhuzhiheng/Desktop/文章/视频资源/douyin/json/creator_contents_2026-02-10.json')
