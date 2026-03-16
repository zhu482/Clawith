#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增量更新向量库
git pull 后运行，只添加新文章
"""

import os
import pickle
import numpy as np
import os
import pickle
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

# 配置
VECTOR_DB_PATH = ".vector_db"
SOURCE_DIRS = ["高质样例/公众号", "视频资源", "openclaw教程/b站参考"] # 支持更多来源
MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
DB_FILE = os.path.join(VECTOR_DB_PATH, 'articles.pkl')

def load_existing_db():
    """加载现有向量库"""
    if not os.path.exists(DB_FILE):
        print("❌ 向量库不存在，请先运行 init_vector_db.py")
        return None
    
    with open(DB_FILE, 'rb') as f:
        data = pickle.load(f)
    
    return data

def get_existing_files(data):
    """获取已索引的文件列表"""
    existing = set()
    for article in data['articles']:
        existing.add(article['file_path'])
    return existing

def find_new_files(directories, existing_files):
    """从多个目录找到新增的文件"""
    new_files = []
    
    for directory in directories:
        if not os.path.exists(directory):
            continue
            
        for root, dirs, files in os.walk(directory):
            # 排除干扰目录
            if any(x in root for x in ['_系统', 'MediaCrawler', '.git', 'videos', 'json', '__pycache__']):
                continue
                
            for file in files:
                filepath = os.path.join(root, file)
                
                # 公众号：索引所有 .md 和 .pdf
                if "高质样例/公众号" in root:
                    if (file.endswith('.md') or file.endswith('.pdf')) and not file.startswith('_'):
                        if filepath not in existing_files:
                            new_files.append(filepath)
                # 视频资源及参考资料：仅索引 README.md (包含音频转出的 README)
                elif any(x in root for x in ["视频资源", "openclaw教程/b站参考"]):
                    if file in ['README.md', 'transcription.md'] or file.endswith('.pdf'):
                        if filepath not in existing_files:
                            new_files.append(filepath)
    
    return new_files

def read_pdf_text(filepath):
    """读取PDF文件的文本内容"""
    text = ""
    try:
        reader = PdfReader(filepath)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"  ⚠️  PDF解析失败: {filepath} - {e}")
    return text

def read_new_articles(filepaths):
    """读取新文章并分块"""
    articles = []
    
    for filepath in filepaths:
        try:
            content = ""
            if filepath.lower().endswith('.pdf'):
                content = read_pdf_text(filepath)
            else:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            
            if not content.strip():
                continue

            chunks = [content[i:i+1000] for i in range(0, len(content), 1000)]
            
            for idx, chunk in enumerate(chunks):
                if len(chunk.strip()) > 100:
                    articles.append({
                        'content': chunk,
                        'file_path': filepath,
                        'chunk_index': idx,
                        'title': os.path.basename(filepath).replace('.md', '').replace('.pdf', '')
                    })
        except Exception as e:
            print(f"  ⚠️  读取失败: {filepath} - {e}")
    
    return articles

def update_vector_db():
    """增量更新向量库"""
    print("🔄 检查向量库更新...")
    print("━" * 50)
    
    # 加载现有数据
    data = load_existing_db()
    if data is None:
        return
    
    existing_files = get_existing_files(data)
    print(f"📊 已索引: {len(existing_files)} 个文件")
    
    # 查找新文件
    new_files = find_new_files(SOURCE_DIRS, existing_files)
    
    if not new_files:
        print("✅ 没有新文章，无需更新")
        return
    
    print(f"📥 发现 {len(new_files)} 个新文件")
    
    # 读取新文章
    new_articles = read_new_articles(new_files)
    if not new_articles:
        print("⚠️  没有有效的新文本块")
        return
    
    print(f"📝 新增 {len(new_articles)} 个文本块")
    
    # 加载模型
    print(f"📥 加载向量化模型: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    
    # 向量化新文章
    print("🔄 正在建立索引...")
    new_texts = [a['content'] for a in new_articles]
    new_embeddings = model.encode(new_texts, show_progress_bar=True)
    
    # 合并数据
    data['articles'].extend(new_articles)
    data['embeddings'] = np.vstack([data['embeddings'], new_embeddings])
    
    # 保存
    with open(DB_FILE, 'wb') as f:
        pickle.dump(data, f)
    
    print()
    print("━" * 50)
    print("🎉 向量库更新完成！")
    print(f"📊 总计: {len(data['articles'])} 个文本块")
    print(f"💾 存储位置: {DB_FILE}")

if __name__ == "__main__":
    update_vector_db()
