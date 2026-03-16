#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试脚本 - 验证 image-generator 功能
"""

import sys
from pathlib import Path

# 添加脚本路径
sys.path.insert(0, str(Path(__file__).parent))

from generate import generate_image, save_image

def test_text_to_image():
    """测试文生图功能"""
    print("=" * 60)
    print("测试 1: 文生图")
    print("=" * 60)
    
    try:
        image_data = generate_image(
            prompt="一只可爱的橘猫在阳光下打哈欠，水彩画风格",
            aspect_ratio="1:1",
            quality="standard"
        )
        
        output_path = save_image(image_data, "test_cat.jpg")
        print(f"✅ 测试通过！图片已保存到: {output_path}\n")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}\n")
        return False


def test_image_to_image():
    """测试图生图功能（需要先有输入图片）"""
    print("=" * 60)
    print("测试 2: 图生图（编辑）")
    print("=" * 60)
    print("⚠️  此测试需要输入图片，跳过...")
    print("使用方法:")
    print("  python3 generate.py -p '将背景改为星空' -i input.jpg -o edited.jpg\n")
    return True


if __name__ == '__main__':
    print("\n🧪 开始测试 image-generator 功能\n")
    
    results = []
    results.append(("文生图", test_text_to_image()))
    results.append(("图生图", test_image_to_image()))
    
    print("=" * 60)
    print("测试结果汇总")
    print("=" * 60)
    
    for name, passed in results:
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"{name}: {status}")
    
    all_passed = all(result[1] for result in results)
    
    if all_passed:
        print("\n🎉 所有测试通过！")
        sys.exit(0)
    else:
        print("\n⚠️  部分测试失败")
        sys.exit(1)
