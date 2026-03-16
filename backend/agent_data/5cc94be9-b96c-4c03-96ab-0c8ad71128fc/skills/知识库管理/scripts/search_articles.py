#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文章检索工具
"""

import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer, util

# 配置
VECTOR_DB_PATH = ".vector_db"
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

def search(query, top_k=10):
    """检索文章"""
    # 加载向量库
    db_file = os.path.join(VECTOR_DB_PATH, 'articles.pkl')
    with open(db_file, 'rb') as f:
        data = pickle.load(f)
    
    articles = data['articles']
    embeddings = data['embeddings']
    
    # 加载模型
    model = SentenceTransformer(MODEL_NAME)
    
    # 向量化查询
    query_embedding = model.encode(query)
    
    # 计算相似度
    similarities = util.cos_sim(query_embedding, embeddings)[0]
    similarities = similarities.cpu().numpy()
    
    # 排序
    top_indices = np.argsort(-similarities)[:top_k]
    
    # 返回结果
    results = []
    for idx in top_indices:
        results.append({
            'score': float(similarities[idx]),
            'file_path': articles[idx]['file_path'],
            'title': articles[idx]['title'],
            'content': articles[idx]['content'][:300],  # 前300字
            'chunk_index': articles[idx]['chunk_index']
        })
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python search_articles.py '查询内容'")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"🔍 检索: {query}")
    print("━" * 60)
    
    results = search(query, top_k=10)
    
    for i, result in enumerate(results, 1):
        print(f"\n【{i}】相关度: {result['score']:.2%}")
        print(f"标题: {result['title']}")
        print(f"文件: {result['file_path']}")
        print(f"片段: {result['content'][:150]}...")
        print("─" * 60)
