#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
商品图参考分析工具
用于在生成前分析参考图并生成策略报告
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

# 导入会话管理
sys.path.insert(0, str(Path(__file__).parent))
from restyle import ProductRestyleSession

def analyze_references(project_name, reference_images, output_root=None):
    """
    分析参考图并生成报告
    
    Args:
        project_name: 项目名称
        reference_images: 参考图路径列表
        output_root: 输出根目录
    """
    session = ProductRestyleSession(project_name, output_root)
    
    print(f"\n📋 开始分析项目: {project_name}")
    print(f"📁 输出目录: {session.project_dir}\n")
    
    # 交互式分析每张参考图
    for idx, img_path in enumerate(reference_images, 1):
        img_name = Path(img_path).name
        print(f"\n{'='*60}")
        print(f"📸 参考图 {idx}/{len(reference_images)}: {img_name}")
        print(f"{'='*60}")
        
        # 获取用户输入
        angle = input(f"  角度 (例: 正面/侧面/后跟/俯拍): ").strip()
        details = input(f"  关键细节 (例: Logo位置、材质特征): ").strip()
        tags_input = input(f"  标签 (用逗号分隔，例: Ref_A, Front, Main): ").strip()
        tags = [t.strip() for t in tags_input.split(',') if t.strip()]
        
        # 添加到会话
        session.add_reference_analysis(img_path, angle, details, tags)
        print(f"  ✅ 已记录")
    
    # 场景设定
    print(f"\n{'='*60}")
    print(f"🎬 场景设定")
    print(f"{'='*60}")
    surface = input("  表面 (例: 深灰色地毯/木地板/白色桌面): ").strip()
    lighting = input("  光线 (例: 自然窗光+暖黄光/冷白吸顶灯): ").strip()
    vibe = input("  氛围 (例: 网感开箱/硬核验货/极简): ").strip() or "clean"
    
    session.set_scene(surface, lighting, vibe)
    
    # 保存报告
    session.save_analysis_report()
    
    print(f"\n{'='*60}")
    print(f"✨ 分析完成！")
    print(f"📄 报告位置: {session.analysis_file}")
    print(f"💡 下一步: 使用 restyle.py 配合 --project {project_name} 生成图片")
    print(f"{'='*60}\n")
    
    return session


def main():
    parser = argparse.ArgumentParser(
        description="商品图参考分析工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 交互式分析
  python3 analyze.py --project "kappa_silver_sneakers" --input img1.jpg img2.jpg img3.jpg
  
  # 指定输出目录
  python3 analyze.py --project "my_product" --input *.jpg --output-root ~/Desktop/商品图
        """
    )
    
    parser.add_argument('--project', required=True, help='项目名称')
    parser.add_argument('--input', '-i', nargs='+', required=True, help='参考图路径')
    parser.add_argument('--output-root', help='输出根目录（默认: ~/Desktop/文章/商品图）')
    
    args = parser.parse_args()
    
    analyze_references(args.project, args.input, args.output_root)


if __name__ == '__main__':
    main()
