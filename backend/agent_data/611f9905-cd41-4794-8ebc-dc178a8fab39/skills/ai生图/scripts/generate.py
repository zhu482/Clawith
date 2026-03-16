#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 图片生成器
支持文生图和图生图（编辑）
基于 Gemini 3 Pro Image API
"""

import os
import sys
import json
import base64
import argparse
import requests
import time
from pathlib import Path
from typing import List, Optional

# API 配置
API_URL = "https://n.lconai.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent"
API_KEY = "sk-S99RMbP5FaEuQEy1v0LTbEo6lsgSmRQjgoSouKA3etGX1GW6"

# 输出目录（从 .agent/skills-v2/04-视觉设计/AI生图/scripts/ 向上6层到达项目根目录）
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent.parent.parent / "创作空间" / "AI生图"

# 支持的图片格式
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.webp'}

# 尺寸配置（根据官方文档）
ASPECT_RATIOS = {
    '1:1': {'width': 1024, 'height': 1024},
    '16:9': {'width': 1376, 'height': 768},
    '9:16': {'width': 768, 'height': 1376},
    '4:3': {'width': 1200, 'height': 896},
    '3:4': {'width': 896, 'height': 1200},
    '3:2': {'width': 1264, 'height': 848},
    '2:3': {'width': 848, 'height': 1264},
}

# 画质配置
QUALITY_SETTINGS = {
    'standard': '1K',
    'high': '2K',
    'ultra': '4K'
}


def encode_image_to_base64(image_path: str) -> tuple:
    """将图片编码为 Base64"""
    path = Path(image_path)
    
    if not path.exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    # 检查文件格式
    if path.suffix.lower() not in SUPPORTED_FORMATS:
        raise ValueError(f"不支持的图片格式: {path.suffix}. 支持的格式: {SUPPORTED_FORMATS}")
    
    # 读取并编码
    with open(path, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')
    
    # 确定 MIME 类型
    mime_type = 'image/jpeg' if path.suffix.lower() in {'.jpg', '.jpeg'} else f'image/{path.suffix[1:]}'
    
    return base64_data, mime_type


def generate_image(
    prompt: str,
    input_images: Optional[List[str]] = None,
    aspect_ratio: str = '1:1',
    quality: str = 'standard',
    max_retries: int = 3
) -> bytes:
    """
    生成或编辑图片
    
    Args:
        prompt: 文字描述或编辑指令
        input_images: 输入图片路径列表（最多3张）
        aspect_ratio: 图片比例
        quality: 画质设置
        max_retries: 最大重试次数
    
    Returns:
        生成的图片数据（bytes）
    """
    # 构建请求内容
    parts = []
    
    # 添加文字提示
    parts.append({"text": prompt})
    
    # 添加输入图片（如果有）
    if input_images:
        if len(input_images) > 3:
            raise ValueError("最多支持 3 张输入图片")
        
        print(f"📦 正在编码 {len(input_images)} 张图片...")
        for i, img_path in enumerate(input_images, 1):
            print(f"   [{i}/{len(input_images)}] {Path(img_path).name}")
            base64_data, mime_type = encode_image_to_base64(img_path)
            parts.append({
                "inlineData": {
                    "mimeType": mime_type,
                    "data": base64_data
                }
            })
        print(f"✅ 图片编码完成")
    
    # 构建完整请求
    payload = {
        "contents": [{
            "parts": parts
        }],
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": QUALITY_SETTINGS.get(quality, '1K')
            }
        },
    }
    
    # 发送请求
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": API_KEY
    }
    
    print(f"\n🎨 正在生成图片...")
    print(f"📝 提示词: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
    if input_images:
        print(f"🖼️  输入图片: {len(input_images)} 张")
    print(f"📐 尺寸: {aspect_ratio}")
    print(f"✨ 画质: {quality}")
    
    # 重试机制
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                print(f"\n🔄 重试 {attempt}/{max_retries}...")
                time.sleep(2 ** attempt)  # 指数退避
            
            print(f"⏳ 正在请求 API（这可能需要 1-3 分钟，请耐心等待）...")
            
            # 增加超时时间到 5 分钟
            response = requests.post(
                API_URL, 
                headers=headers, 
                json=payload, 
                timeout=300,  # 5分钟超时
                stream=False
            )
            
            print(f"📡 收到响应，状态码: {response.status_code}")
            response.raise_for_status()
            
            result = response.json()
            
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    for part in candidate['content']['parts']:
                        # Handle both 'inlineData' and 'inline_data'
                        image_part = part.get('inlineData') or part.get('inline_data')
                        if image_part:
                            print(f"🎉 图片生成成功，正在解码...")
                            # 解码 Base64 图片数据
                            image_base64 = image_part['data']
                            image_bytes = base64.b64decode(image_base64)
                            return image_bytes
            
            # 如果没有找到图片，打印返回的结果以便调试
            print(f"⚠️  API 返回了数据，但没有找到图片")
            print(f"DEBUG: API Response: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}...")
            
            if attempt < max_retries - 1:
                continue
            else:
                raise ValueError("API 返回的数据中没有找到图片")
            
        except requests.exceptions.Timeout:
            print(f"⏱️  请求超时（尝试 {attempt + 1}/{max_retries}）")
            if attempt < max_retries - 1:
                continue
            else:
                raise Exception("请求超时，请检查网络连接或稍后重试")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 网络请求失败: {str(e)}")
            if e.response is not None:
                print(f"DEBUG: Error Response: {e.response.text[:500]}")
            if attempt < max_retries - 1:
                continue
            else:
                raise Exception(f"API 请求失败: {str(e)}")
                
        except Exception as e:
            print(f"❌ 发生错误: {str(e)}")
            if attempt < max_retries - 1:
                continue
            else:
                raise Exception(f"生成图片时出错: {str(e)}")


def save_image(image_data: bytes, output_path: str):
    """保存图片到文件"""
    path = Path(output_path)
    
    # 如果是相对路径，保存到默认输出目录
    if not path.is_absolute():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = OUTPUT_DIR / path.name
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'wb') as f:
        f.write(image_data)
    
    print(f"✅ 图片已保存: {path}")
    return path


def main():
    parser = argparse.ArgumentParser(
        description="AI 图片生成器 - 支持文生图和图生图",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 文生图
  %(prog)s --prompt "一只可爱的橘猫" --output cat.jpg
  
  # 图生图（编辑）
  %(prog)s --prompt "将背景改为星空" --input photo.jpg --output edited.jpg
  
  # 多图合成
  %(prog)s --prompt "合成这两张图" --input img1.jpg img2.jpg --output combined.jpg
        """
    )
    
    parser.add_argument('--prompt', '-p', required=True, help='文字描述或编辑指令')
    parser.add_argument('--output', '-o', required=True, help='输出文件路径')
    parser.add_argument('--input', '-i', nargs='+', help='输入图片路径（最多3张）')
    parser.add_argument(
        '--aspect-ratio', '-r',
        choices=list(ASPECT_RATIOS.keys()),
        default='1:1',
        help='图片比例（默认: 1:1）'
    )
    parser.add_argument(
        '--quality', '-q',
        choices=list(QUALITY_SETTINGS.keys()),
        default='standard',
        help='画质设置（默认: standard）'
    )
    
    args = parser.parse_args()
    
    try:
        # 生成图片
        image_data = generate_image(
            prompt=args.prompt,
            input_images=args.input,
            aspect_ratio=args.aspect_ratio,
            quality=args.quality
        )
        
        # 保存图片
        output_path = save_image(image_data, args.output)
        
        print(f"\n🎉 生成成功!")
        print(f"📁 文件位置: {output_path}")
        print(f"📊 文件大小: {len(image_data) / 1024:.2f} KB")
        
    except Exception as e:
        print(f"\n❌ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
