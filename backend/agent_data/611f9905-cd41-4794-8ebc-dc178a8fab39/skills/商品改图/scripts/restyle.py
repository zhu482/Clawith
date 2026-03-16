#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
得物/小红书商品改图助手 v2.0
- 支持分析报告生成
- 支持项目目录管理
- 支持参考图分配记录
"""

import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# 获取 generate.py 的路径（新架构：06-工作辅助/商品改图/scripts/ → 04-视觉设计/AI生图/scripts/）
# 从当前目录向上4层到.agent/skills-v2/，然后进入04-视觉设计/AI生图/scripts/
GENERATE_SCRIPT = Path(__file__).parent.parent.parent.parent / "04-视觉设计" / "AI生图" / "scripts" / "generate.py"

# 默认输出根目录
DEFAULT_OUTPUT_ROOT = Path.home() / "Desktop" / "文章" / "商品图"

class ProductRestyleSession:
    """商品改图会话管理"""
    
    def __init__(self, project_name, output_root=None):
        self.project_name = project_name
        self.output_root = Path(output_root) if output_root else DEFAULT_OUTPUT_ROOT
        self.project_dir = self.output_root / project_name
        self.project_dir.mkdir(parents=True, exist_ok=True)
        
        # 分析报告路径
        self.analysis_file = self.project_dir / "analysis_report.md"
        
        # 会话数据
        self.session_data = {
            "project_name": project_name,
            "created_at": datetime.now().isoformat(),
            "reference_images": [],
            "scene_setting": {},
            "generation_tasks": []
        }
    
    def add_reference_analysis(self, image_path, angle, details, tags):
        """添加参考图分析"""
        ref_data = {
            "file": str(image_path),
            "angle": angle,
            "details": details,
            "tags": tags
        }
        self.session_data["reference_images"].append(ref_data)
    
    def set_scene(self, surface, lighting, vibe="clean"):
        """设置场景"""
        self.session_data["scene_setting"] = {
            "surface": surface,
            "lighting": lighting,
            "vibe": vibe
        }
    
    def add_generation_task(self, task_name, ref_images, prompt, output_file):
        """添加生成任务"""
        task = {
            "name": task_name,
            "reference_images": ref_images,
            "prompt": prompt,
            "output": str(output_file),
            "timestamp": datetime.now().isoformat()
        }
        self.session_data["generation_tasks"].append(task)
    
    def save_analysis_report(self):
        """保存分析报告为 Markdown"""
        with open(self.analysis_file, 'w', encoding='utf-8') as f:
            f.write(f"# 商品改图分析报告\n\n")
            f.write(f"**项目名称**: {self.project_name}\n\n")
            f.write(f"**创建时间**: {self.session_data['created_at']}\n\n")
            f.write(f"**输出目录**: `{self.project_dir}`\n\n")
            f.write("---\n\n")
            
            # 参考图分析
            f.write("## 📸 参考图分析 (Reference Analysis)\n\n")
            for idx, ref in enumerate(self.session_data["reference_images"], 1):
                f.write(f"### Ref_{chr(64+idx)}: `{Path(ref['file']).name}`\n\n")
                f.write(f"- **角度**: {ref['angle']}\n")
                f.write(f"- **细节**: {ref['details']}\n")
                f.write(f"- **标签**: {', '.join(ref['tags'])}\n\n")
            
            # 场景设定
            f.write("---\n\n")
            f.write("## 🎬 场景设定 (Scene Setting)\n\n")
            scene = self.session_data["scene_setting"]
            if scene:
                f.write(f"- **表面**: {scene.get('surface', 'N/A')}\n")
                f.write(f"- **光线**: {scene.get('lighting', 'N/A')}\n")
                f.write(f"- **氛围**: {scene.get('vibe', 'N/A')}\n\n")
            
            # 生成任务
            f.write("---\n\n")
            f.write("## 🖼️ 生成任务 (Generation Tasks)\n\n")
            for idx, task in enumerate(self.session_data["generation_tasks"], 1):
                f.write(f"### {idx}. {task['name']}\n\n")
                f.write(f"- **参考图**: {', '.join([Path(r).name for r in task['reference_images']])}\n")
                f.write(f"- **提示词**:\n```\n{task['prompt']}\n```\n")
                f.write(f"- **输出文件**: `{Path(task['output']).name}`\n")
                f.write(f"- **生成时间**: {task['timestamp']}\n\n")
        
        print(f"✅ 分析报告已保存: {self.analysis_file}")
    
    def get_output_path(self, filename):
        """获取输出文件路径"""
        return self.project_dir / filename


def run_restyle(inputs, output, scene="indoor", custom_prompt="", aspect_ratio="3:4", 
                project_name=None, session=None):
    """执行改图"""
    # 基础风格 Token
    style_tokens = (
        "Shot on iPhone, bright and well-lit, authentic and unedited look, amateur snapshot, "
        "no professional heavy bokeh, everything in sharp focus unless it is a macro shot, "
        "domestic Chinese vibe, high realism, clean and airy atmosphere, NO dark or gloomy lighting."
    )
    
    # 场景逻辑
    if scene == "indoor":
        scene_desc = (
            "The product is placed on a clean, ordinary domestic surface (like a wooden table, white desk, or carpet). "
            "Bright and natural indoor lighting, soft window light mixed with warm-white interior light, "
            "vivid colors, NO deep shadows, clean and high-key background."
        )
    else:
        scene_desc = (
            "The product is placed on a sunlit concrete pavement or an ordinary park bench in a Chinese city. "
            "Natural bright daylight, realistic outdoor atmosphere, normal street road texture."
        )

    # 组合最终 Prompt
    final_prompt = f"{custom_prompt}. Scenario: {scene_desc} Style: {style_tokens}"
    
    # 如果有 session，记录任务
    if session:
        session.add_generation_task(
            task_name=Path(output).stem,
            ref_images=inputs,
            prompt=final_prompt,
            output_file=output
        )
    
    # 构建命令
    cmd = [
        "python3",
        str(GENERATE_SCRIPT),
        "--prompt", f'"{final_prompt}"',
        "--output", f'"{output}"',
        "--aspect-ratio", aspect_ratio,
        "--quality", "standard"
    ]
    
    if inputs:
        cmd.append("--input")
        cmd.extend([f'"{i}"' for i in inputs])
    
    cmd_str = " ".join(cmd)
    print(f"🚀 执行改图命令: {cmd_str}")
    os.system(cmd_str)


def main():
    parser = argparse.ArgumentParser(description="得物/小红书商品改图助手 v2.0")
    parser.add_argument('--input', '-i', nargs='+', required=True, help='输入商品图路径')
    parser.add_argument('--output', '-o', required=True, help='输出文件名')
    parser.add_argument('--scene', '-s', choices=['indoor', 'outdoor'], default='indoor', help='场景类型')
    parser.add_argument('--prompt', '-p', default='', help='基础商品描述或额外要求')
    parser.add_argument('--aspect-ratio', '-r', default='3:4', help='比例')
    parser.add_argument('--project', required=False, help='项目名称（用于组织输出目录）')
    parser.add_argument('--output-root', help='输出根目录（默认: ~/Desktop/文章/商品图）')

    args = parser.parse_args()
    
    # 如果指定了项目名称，使用会话管理
    if args.project:
        session = ProductRestyleSession(args.project, args.output_root)
        output_path = session.get_output_path(Path(args.output).name)
        run_restyle(args.input, str(output_path), args.scene, args.prompt, args.aspect_ratio, 
                   args.project, session)
        session.save_analysis_report()
    else:
        # 兼容旧模式
        run_restyle(args.input, args.output, args.scene, args.prompt, args.aspect_ratio)


if __name__ == '__main__':
    main()
