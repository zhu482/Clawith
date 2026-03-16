#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
初始化向量库
首次使用或新电脑上运行一次即可
"""

import os
import pickle
from sentence_transformers import SentenceTransformer

# 配置
VECTOR_DB_PATH = ".vector_db"
ARTICLES_DIR = "高质样例/公众号"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"  # 支持中文的轻量模型

def read_markdown_files(directory):
    """递归读取所有markdown文件"""
    articles = []
    
    for root, dirs, files in os.walk(directory):
        # 跳过系统目录
        if '_系统' in root:
            continue
            
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # 简单分块（每1000字一块）
                    chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
                    
                    for idx, chunk in enumerate(chunks):
                        if len(chunk.strip()) > 100:  # 过滤太短的块
                            articles.append({
                                'content': chunk,
                                'file_path': filepath,
                                'chunk_index': idx,
                                'title': file.replace('.md', '')
                            })
                except Exception as e:
                    print(f"  ⚠️  读取失败: {filepath} - {e}")
    
    return articles

def init_vector_db():
    """初始化向量库"""
    print("🚀 开始初始化向量库...")
    print("━" * 50)
    
    # 创建向量库目录
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    
    # 加载模型
    print(f"📥 加载向量化模型: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    print("✅ 模型加载完成")
    
    # 读取文章
    print(f"📖 读取文章: {ARTICLES_DIR}")
    articles = read_markdown_files(ARTICLES_DIR)
    print(f"✅ 找到 {len(articles)} 个文本块")
    
    if not articles:
        print("❌ 没有找到文章，请检查目录")
        return
    
    # 向量化
    print("🔄 正在建立索引...")
    texts = [a['content'] for a in articles]
    embeddings = model.encode(texts, show_progress_bar=True)
    
    # 保存
    data = {
        'articles': articles,
        'embeddings': embeddings
    }
    
    db_file = os.path.join(VECTOR_DB_PATH, 'articles.pkl')
    with open(db_file, 'wb') as f:
        pickle.dump(data, f)
    
    print()
    print("━" * 50)
    print("🎉 向量库初始化完成！")
    print(f"📊 总计: {len(articles)} 个文本块")
    print(f"💾 存储位置: {db_file}")
    print()
    print("现在可以使用检索功能了！")

if __name__ == "__main__":
    init_vector_db()
