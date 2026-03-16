#!/usr/bin/env python3
import os
import sys
import uuid
import subprocess
import shutil

def check_dependencies():
    """Check if ffmpeg and exiftool are installed."""
    missing = []
    if not shutil.which('ffmpeg'):
        missing.append('ffmpeg')
    if not shutil.which('exiftool'):
        missing.append('exiftool')
    
    if missing:
        print("❌ Error: Missing required tools:", ", ".join(missing))
        print("Please install them using brew:")
        print(f"  brew install {' '.join(missing)}")
        sys.exit(1)

def convert_to_live_photo(video_path):
    if not os.path.exists(video_path):
        print(f"❌ Error: File '{video_path}' not found.")
        return

    # Normalize paths
    video_path = os.path.abspath(video_path)
    directory = os.path.dirname(video_path)
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Output paths
    jpg_path = os.path.join(directory, f"{base_name}.JPG")
    mov_path = os.path.join(directory, f"{base_name}.MOV")
    
    print(f"🎬 Processing: {os.path.basename(video_path)}")

    # 1. Generate JPG cover (extract first frame)
    # Using 00:00:00 to ensure start sync. 
    # -q:v 2 ensures high quality JPEG.
    print(f"📸 Extracting cover image...")
    try:
        subprocess.run([
            'ffmpeg', '-y', 
            '-i', video_path, 
            '-ss', '00:00:00', 
            '-vframes', '1', 
            '-q:v', '2', 
            jpg_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print("❌ Failed to extract frame with ffmpeg.")
        print(e.stderr.decode() if e.stderr else "Unknown error")
        return

    # 2. Process Video (Convert/Copy to MOV)
    # We always create a .MOV file. If input is mp4, we copy stream.
    print(f"🎥 Preparing video file...")
    if video_path != mov_path:
        try:
            subprocess.run([
                'ffmpeg', '-y',
                '-i', video_path,
                '-c', 'copy',
                '-f', 'mov',
                mov_path
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print("❌ Failed to convert video with ffmpeg.")
            print(e.stderr.decode() if e.stderr else "Unknown error")
            return
    else:
        print(f"   Input is already the target .MOV file. Using in-place (backup recommended).")

    # 3. Generate UUID and write metadata
    # This UUID links the photo and video together.
    asset_id = str(uuid.uuid4()).upper()
    print(f"🔗 Linking with Asset ID: {asset_id}")
    
    try:
        # Write to JPG (Apple MakerNote)
        # Using -ContentIdentifier assumes exiftool < 12.00 or specific config, 
        # but typically -MakerNotes:ContentIdentifier works best if explicitly supported.
        # More generic approach that usually works on modern exiftool:
        subprocess.run([
            'exiftool', 
            '-overwrite_original',
            f'-ContentIdentifier={asset_id}',
            jpg_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        
        # Write to MOV (QuickTime Key)
        subprocess.run([
            'exiftool',
            '-overwrite_original', 
            f'-ContentIdentifier={asset_id}',
            mov_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        
    except subprocess.CalledProcessError as e:
        print("❌ Failed to write metadata with exiftool.")
        print(e.stderr.decode() if e.stderr else "Unknown error")
        return
    
    print("\n✅ Success! Live Photo pair created:")
    print(f"  📂 Image: {os.path.basename(jpg_path)}")
    print(f"  📂 Video: {os.path.basename(mov_path)}")
    print("\n👉 To use: Import BOTH files together into Photos app on Mac, or AirDrop BOTH to iPhone.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 video_to_live.py <video_file>")
        sys.exit(1)
        
    check_dependencies()
    convert_to_live_photo(sys.argv[1])
