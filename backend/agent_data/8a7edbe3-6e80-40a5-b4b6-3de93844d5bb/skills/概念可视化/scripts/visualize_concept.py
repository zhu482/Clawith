#!/usr/bin/env python3
"""
Concept Visualizer Script (v5.0 - Professional Designer Edition)

"""

import sys
import os
import argparse
import time

# --- Configuration ---
GENERATOR_LIB_PATH = "/Users/zhuzhiheng/Desktop/zz知识库/小红书/图文生成器"
if GENERATOR_LIB_PATH not in sys.path:
    sys.path.append(GENERATOR_LIB_PATH)

try:
    from generate_ai_image import generate_and_crop_image
except ImportError:
    print(f"❌ Error: Cannot find 'generate_ai_image.py'")
    sys.exit(1)

# --- Visual Style Constants ---
# --- Visual Style Constants ---
# (Style instructions should be provided in the input prompt by the Agent based on SKILL.md)

def generate_with_retry(prompt, output_path, ratio="16:9", max_retries=3):
    size = "2752x1536"
    attempt = 1
    while attempt <= max_retries:
        print(f"🎨 Attempt {attempt}...")
        try:
            # Let the prompt drive the style (style=None by default now)
            result = generate_and_crop_image(prompt, output_path, ratio=ratio, size=size)
            if result and os.path.exists(result):
                return result
        except Exception as e:
            print(f"⚠️ Error: {str(e)}")
        time.sleep(2)
        attempt += 1
    return None

def main():
    parser = argparse.ArgumentParser(description="Concept Visualizer v5.0 (Professional Designer Edition)")
    parser.add_argument("--type", required=True)
    parser.add_argument("--ratio", default="16:9")
    parser.add_argument("--output", required=True)
    parser.add_argument("--data", help="Content description")
    args = parser.parse_args()

    output_full_path = os.path.abspath(args.output)

    # Use data directly
    # The prompt is fully constructed by the Agent Skill, so we just pass it through.
    full_prompt = args.data if args.data else "Test Diagram"

    print(f"🚀 生成精致理性的知识卡片: {os.path.basename(output_full_path)}")
    result = generate_with_retry(full_prompt, output_full_path, ratio="16:9")
    
    if result:
        print(f"✅ Saved to: {result}")
    else:
        print("❌ Failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
