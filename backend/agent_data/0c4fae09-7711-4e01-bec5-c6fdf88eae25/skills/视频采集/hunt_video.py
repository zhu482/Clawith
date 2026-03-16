#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video Hunter - 全能视频搜索与下载工具
支持多平台 (B站/抖音/小红书等) 的 搜索/详情/主页 爬取，并自动整理转写。
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path

# 路径配置
PROJECT_ROOT = Path(os.getcwd())
MEDIACRAWLER_DIR = PROJECT_ROOT / "MediaCrawler"
CONFIG_FILE = MEDIACRAWLER_DIR / "config" / "base_config.py"
ORGANIZE_SCRIPT = PROJECT_ROOT / "视频资源" / "organize_media.py"

# 默认配置
DEFAULT_LIMIT = 20
SUPPORTED_PLATFORMS = ["bili", "dy", "xhs", "ks", "wb", "tieba", "zhihu"]

class ConfigManager:
    """临时修改 MediaCrawler 配置文件"""
    def __init__(self, config_path, args):
        self.config_path = config_path
        self.args = args
        self.original_content = None

    def __enter__(self):
        if not self.config_path.exists():
            print(f"⚠️ 警告: 配置文件未找到 {self.config_path}，跳过修改配置")
            return

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.original_content = f.read()
            
            new_content = self.original_content
            
            # 1. 数量限制
            new_content = re.sub(
                r'CRAWLER_MAX_NOTES_COUNT\s*=\s*\d+', 
                f'CRAWLER_MAX_NOTES_COUNT = {self.args.count}', 
                new_content
            )
            
            # 2. 词云图
            wordcloud_val = "True" if self.args.wordcloud else "False"
            new_content = re.sub(
                r'ENABLE_GET_WORDCLOUD\s*=\s*\w+', 
                f'ENABLE_GET_WORDCLOUD = {wordcloud_val}', 
                new_content
            )

            # 3. 媒体下载控制 (只有明确要求下载时才开启)
            download_val = "True" if self.args.download else "False"
            new_content = re.sub(
                r'ENABLE_GET_MEIDAS\s*=\s*\w+', 
                f'ENABLE_GET_MEIDAS = {download_val}', 
                new_content
            )

            # 4. 评论抓取控制 (默认关闭，除非显式指定)
            comment_val = "True" if self.args.get_comment else "False"
            new_content = re.sub(
                r'ENABLE_GET_COMMENTS\s*=\s*\w+', 
                f'ENABLE_GET_COMMENTS = {comment_val}', 
                new_content
            )
            
            with open(self.config_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"⚙️ 临时调整配置 (Count: {self.args.count}, Download: {self.args.download}, Comments: {self.args.get_comment})")
        except Exception as e:
            print(f"⚠️ 修改配置失败: {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.original_content:
            try:
                with open(self.config_path, 'w', encoding='utf-8') as f:
                    f.write(self.original_content)
            except Exception as e:
                print(f"⚠️ 恢复配置失败: {e}")

def run_mediacrawler(args):
    """根据参数构建并运行 MediaCrawler 命令"""
    print(f"\n🚀 [1/2] 启动 MediaCrawler ({args.platform} | {args.type})...")
    
    cmd = ["uv", "run", "main.py", "--platform", args.platform, "--lt", args.login_type]
    
    # 根据类型映射参数
    if args.type == "search":
        cmd.extend(["--type", "search", "--keywords", args.query])
    elif args.type == "detail":
        cmd.extend(["--type", "detail", "--specified_id", args.query])
    elif args.type == "creator":
        cmd.extend(["--type", "creator", "--creator_id", args.query])
    
    # 评论控制
    cmd.extend(["--get_comment", "true" if args.get_comment else "false"])
    if args.get_sub_comment:
        cmd.extend(["--get_sub_comment", "true"])
    cmd.extend(["--max_comments_count_singlenotes", str(args.max_comments)])
    
    # 其他控制
    if args.headless:
        cmd.extend(["--headless", "true"])
    if args.start_page != 1:
        cmd.extend(["--start", str(args.start_page)])
    if args.max_concurrency != 1:
        cmd.extend(["--max_concurrency_num", str(args.max_concurrency)])
    if args.cookies:
        cmd.extend(["--cookies", args.cookies])
    if args.output_dir:
        cmd.extend(["--save_data_path", args.output_dir])
    
    # 打印简略命令
    print(f"执行任务: 获取 '{args.query}' (Limit: {args.count})")
    
    # 使用 ConfigManager 上下文管理来临时修改配置
    with ConfigManager(CONFIG_FILE, args):
        try:
            subprocess.run(
                cmd,
                cwd=str(MEDIACRAWLER_DIR),
                check=True
            )
            print("✅ MediaCrawler 任务完成")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ MediaCrawler 执行中断 (Exit: {e.returncode})")
            return False
        except KeyboardInterrupt:
            print("\n🛑 用户手动停止任务")
            return False

import json
from datetime import datetime

def display_results(platform):
    """读取最新的 JSON 元数据并展示为 Markdown 表格"""
    # 平台名称映射 (CLI 简称 -> 实际目录名)
    PLATFORM_MAP = {
        "dy": "douyin",
        "xhs": "xhs",
        "bili": "bili",
        "ks": "kuaishou",
        "wb": "weibo",
        "tieba": "tieba",
        "zhihu": "zhihu"
    }
    dir_name = PLATFORM_MAP.get(platform, platform)
    
    # 尝试多个可能的路径
    possible_dirs = []
    
    # 1. 尝试从 config.py 读取 (最准确)
    try:
        import sys
        sys.path.append(str(MEDIACRAWLER_DIR))
        from config import base_config
        if hasattr(base_config, "SAVE_DATA_PATH") and base_config.SAVE_DATA_PATH:
            possible_dirs.append(Path(base_config.SAVE_DATA_PATH) / dir_name / "json")
    except:
        pass
        
    # 2. 尝试默认路径
    possible_dirs.append(MEDIACRAWLER_DIR / "data" / dir_name / "json")
    
    # 3. 尝试项目根目录下的视频资源目录
    possible_dirs.append(PROJECT_ROOT / "视频资源" / dir_name / "json")

    json_dir = None
    for d in possible_dirs:
        if d.exists():
            json_dir = d
            break
            
    if not json_dir:
        print(f"⚠️ 未找到数据目录，已检查以下位置:")
        for d in possible_dirs: print(f"  - {d}")
        return

    json_files = sorted(list(json_dir.glob("*_contents_*.json")), reverse=True)
    if not json_files:
        print("ℹ️ 未发现相关搜索结果。")
        return

    latest_json = json_files[0]
    try:
        with open(latest_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取结果失败: {e}")
        return

    if not data:
        print("ℹ️ 搜索结果为空。")
        return

    if not isinstance(data, list):
        data = [data]

    print("\n### 🔍 搜索结果预览")
    print("| 类型 | 标题 | 博主 | 发布时间 | 链接 |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    
    for item in data[:20]: # 最多展示 20 条
        # 识别类型 (视频 vs 图文)
        raw_type = item.get("type", "").lower()
        if raw_type == "video":
            type_icon = "🎥 视频"
        elif raw_type in ["normal", "image"]:
            type_icon = "🖼️ 图文"
        else:
            # 根据是否有 video_url 二次判定
            type_icon = "🎥 视频" if item.get("video_url") else "🖼️ 图文"

        title = item.get("title") or item.get("desc") or "无标题"
        title = title.replace("|", "\\|").replace("\n", " ").strip()[:50]
        nickname = item.get("nickname") or item.get("user_id") or "未知"
        # video_id = item.get("video_id") or item.get("note_id") or item.get("aweme_id") or "N/A"
        url = item.get("video_url") or item.get("note_url") or "N/A"
        
        create_time = item.get("create_time") or item.get("time") or item.get("timestamp")
        date_str = "未知"
        if create_time:
            try:
                ts = int(create_time)
                # 兼容 13 位和 10 位时间戳
                if ts > 10000000000: ts /= 1000
                date_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            except: pass
            
        print(f"| {type_icon} | {title} | {nickname} | {date_str} | [打开]({url}) |")
    
    print(f"\n> 💡 共有 {len(data)} 条结果。如需下载，请在命令中加入 `--download` 参数。\n")

def run_organizer(platform, output_dir=None, keep_media=False, keyword=None):
    """运行整理和转写脚本"""
    print(f"\n📦 [2/2] 正在整理资源并触发转写 (保留原始文件: {keep_media})...")
    
    if not ORGANIZE_SCRIPT.exists():
        print(f"❌ 错误: 未找到整理脚本: {ORGANIZE_SCRIPT}")
        return False
        
    try:
        cmd = [sys.executable, str(ORGANIZE_SCRIPT), "--platform", platform]
        if output_dir:
            cmd.extend(["--output", str(output_dir)])
        if keep_media:
            cmd.append("--keep-media")
        if keyword:
            cmd.extend(["--keyword", keyword])
            
        subprocess.run(
            cmd,
            cwd=str(PROJECT_ROOT),
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        print("❌ 整理过程出现错误")
        return False

def check_login_status(platform):
    """检测指定平台是否已有登录缓存"""
    # MediaCrawler 默认存储路径
    browser_data_dir = MEDIACRAWLER_DIR / "browser_data"
    cdp_dir = browser_data_dir / f"cdp_{platform}_user_data_dir"
    normal_dir = browser_data_dir / f"{platform}_user_data_dir"
    
    # 如果任意一个目录存在且包含内容，视为可能已登录
    if (cdp_dir.exists() and any(cdp_dir.iterdir())) or \
       (normal_dir.exists() and any(normal_dir.iterdir())):
        return True
    return False

def main():
    parser = argparse.ArgumentParser(
        description="Video Hunter - 全能视频猎手 (搜索/下载/转写)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # 核心参数: 查询内容 (关键词 或 ID)
    parser.add_argument("query", help="搜索关键词 或 视频ID/用户ID")
    
    # 选项参数
    parser.add_argument("--platform", "-p", default="bili", choices=SUPPORTED_PLATFORMS,
                        help="目标平台 (默认: bili)")
    
    parser.add_argument("--type", "-t", default="auto", choices=["auto", "search", "detail", "creator"],
                        help="""操作类型:
  search  : 关键词搜索 (默认: 当输入看起来像关键词时)
  detail  : 下载指定视频 (默认: 当输入看起来像ID时)
  creator : 爬取主页
  auto    : 自动推断 (目前默认为 search)""")
    
    parser.add_argument("--count", "-c", type=int, default=DEFAULT_LIMIT,
                        help=f"爬取数量限制 (仅 Search/Creator 模式有效, 默认: {DEFAULT_LIMIT})")
    
    parser.add_argument("--download", action="store_true",
                        help="是否下载视频并进行后处理 (必须开启此项才能生成详细MD)")

    parser.add_argument("--keep-media", action="store_true",
                        help="是否保留视频/音频文件 (默认: 否, 仅保留MD和Metadata)")

    parser.add_argument("--get-comment", action="store_true", default=False,
                        help="是否爬取一级评论 (默认: 否)")

    parser.add_argument("--get-sub-comment", action="store_true",
                        help="是否爬取二级评论 (默认: 否)")
    
    parser.add_argument("--max-comments", type=int, default=10,
                        help="每个视频/帖子的一级评论数量限制 (默认: 10)")

    parser.add_argument("--login-type", "-l", default="qrcode", choices=["qrcode", "phone", "cookie"],
                        help="登录方式 (默认: qrcode)")

    parser.add_argument("--cookies", help="Cookie 登录模式下的 Cookie 字符串")

    parser.add_argument("--headless", action="store_true", default=None,
                        help="强制启用无头模式")
    parser.add_argument("--no-headless", action="store_false", dest="headless",
                        help="强制禁用无头模式 (以便扫码)")

    parser.add_argument("--start-page", type=int, default=1,
                        help="爬取起始页码 (默认: 1)")

    parser.add_argument("--max-concurrency", type=int, default=1,
                        help="并发爬虫数量 (默认: 1)")

    parser.add_argument("--output-dir", help="指定保存和归档的根目录 (默认: 视频资源/)")

    parser.add_argument("--wordcloud", action="store_true",
                        help="是否生成评论词云图 (仅 JSON 模式有效)")
    
    args = parser.parse_args()
    
    # 自动推断逻辑
    if args.type == "auto":
        # 1. 检查是否是 URL
        if args.query.startswith("http"):
            # 如果包含 'user' 或 'home'，可能是博主主页
            if any(x in args.query.lower() for x in ["user", "home", "profile", "creator"]):
                args.type = "creator"
            else:
                args.type = "detail"
        # 2. 检查是否是常见的 ID 格式
        elif re.match(r'^(BV|av|BV)[a-zA-Z0-9]+$', args.query):
            args.type = "detail"
        # 3. 默认搜索
        else:
            args.type = "search"
    
    # 无头模式自动切换逻辑
    is_logged_in = check_login_status(args.platform)
    if args.headless is None:
        if is_logged_in:
            args.headless = True
            # print(f"✨ 检测到 {args.platform} 已有登录缓存，自动开启无头模式运行")
        else:
            args.headless = False
            print(f"🔑 检测到 {args.platform} 未登录或缓存失效，将打开浏览器窗口以便扫码")
    
    # 如果是下载模式且未登录，强制建议显示界面
    if args.download and not is_logged_in and args.headless:
        print("⚠️ 警告: 您开启了无头下载模式但未检测到登录态，如果需要扫码，请使用 --no-headless")

    # 1. 运行爬虫 (带配置修改)
    if run_mediacrawler(args):
        # 2. 展示结果预览 (MD 表格)
        display_results(args.platform)
        
        # 3. 只有明确要求下载时，才进行整理和归档
        if args.download:
            # 仅在 search 模式下传入 keyword 进行分组，其他模式(detail/creator)由 organizer 自动使用作者名分组
            group_keyword = args.query if args.type == "search" else None
            run_organizer(args.platform, output_dir=args.output_dir, keep_media=args.keep_media, keyword=group_keyword)
        else:
            print("💡 提示: 当前为预览模式，未下载视频文件。如需下载并转写，请添加 --download 参数。")
        
    print("\n🎉 流程结束")

if __name__ == "__main__":
    main()

