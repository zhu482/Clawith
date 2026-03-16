import json
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体 (针对 Mac)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def draw_real_chart(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 抽取前 10 个视频的数据做演示
    titles = []
    likes = []
    collects = []
    
    # 截取前 10 条，并缩短标题
    for item in data[:10]:
        title = item.get('title', '')[:10] + '...'
        titles.append(title)
        likes.append(int(item.get('liked_count', 0)))
        collects.append(int(item.get('collected_count', 0)))

    x = np.arange(len(titles))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width/2, likes, width, label='点赞', color='#3498db')
    rects2 = ax.bar(x + width/2, collects, width, label='收藏', color='#e74c3c')

    ax.set_ylabel('数值')
    ax.set_title('斜杠青年小冯：近期视频互动数据 (真实代码绘制)')
    ax.set_xticks(x)
    ax.set_xticklabels(titles, rotation=45, ha='right')
    ax.legend()

    fig.tight_layout()
    plt.savefig('creator_real_data_chart.png')
    print("✅ 真实图表已生成: creator_real_data_chart.png")

if __name__ == "__main__":
    draw_real_chart('/Users/zhuzhiheng/Desktop/文章/视频资源/douyin/json/creator_contents_2026-02-10.json')
