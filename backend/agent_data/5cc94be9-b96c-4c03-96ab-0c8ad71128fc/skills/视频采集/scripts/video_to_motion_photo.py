#!/usr/bin/env python3
"""
Convert video to Android Motion Photo format.
Motion Photo = JPG image + MP4 video appended + XMP metadata
"""
import os
import sys
import subprocess
import shutil
from datetime import datetime

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

def get_file_size(file_path):
    """Get file size in bytes."""
    return os.path.getsize(file_path)

def create_motion_photo(video_path, output_path=None):
    """
    Create Android Motion Photo from video.

    Args:
        video_path: Path to input video file
        output_path: Optional output path for the motion photo
    """
    if not os.path.exists(video_path):
        print(f"❌ Error: File '{video_path}' not found.")
        return

    # Normalize paths
    video_path = os.path.abspath(video_path)
    directory = os.path.dirname(video_path)
    base_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create temp directory for intermediate files
    temp_dir = os.path.join(directory, '.motion_photo_temp')
    os.makedirs(temp_dir, exist_ok=True)

    # Temp file paths
    jpg_temp = os.path.join(temp_dir, 'image.jpg')
    mp4_temp = os.path.join(temp_dir, 'video.mp4')

    # Output path
    if output_path is None:
        output_path = os.path.join(directory, f"{base_name}_motion.jpg")

    print(f"🎬 Processing: {os.path.basename(video_path)}")

    try:
        # Step 1: Extract first frame as JPG
        print("📸 Extracting cover image...")
        subprocess.run([
            'ffmpeg', '-y',
            '-i', video_path,
            '-ss', '00:00:00',
            '-vframes', '1',
            '-q:v', '2',
            jpg_temp
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        # Step 2: Convert video to MP4 (if not already)
        print("🎥 Preparing video...")
        subprocess.run([
            'ffmpeg', '-y',
            '-i', video_path,
            '-c:v', 'libx264',  # AVC codec for compatibility
            '-c:a', 'aac',
            '-movflags', '+faststart',
            '-preset', 'medium',
            mp4_temp
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        # Step 3: Get file sizes
        jpg_size = get_file_size(jpg_temp)
        mp4_size = get_file_size(mp4_temp)

        print(f"📊 Image size: {jpg_size:,} bytes")
        print(f"📊 Video size: {mp4_size:,} bytes")

        # Step 4: Concatenate JPG + MP4
        print("🔗 Creating Motion Photo...")
        with open(output_path, 'wb') as output_file:
            # Write JPG
            with open(jpg_temp, 'rb') as jpg_file:
                output_file.write(jpg_file.read())
            # Append MP4
            with open(mp4_temp, 'rb') as mp4_file:
                output_file.write(mp4_file.read())

        # Step 5: Add XMP metadata
        print("📝 Writing metadata...")

        # Google Camera XMP namespace for Motion Photo
        xmp_metadata = f"""<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:GCamera="http://ns.google.com/photos/1.0/camera/"
      xmlns:Container="http://ns.google.com/photos/1.0/container/"
      xmlns:Item="http://ns.google.com/photos/1.0/container/item/"
      GCamera:MotionPhoto="1"
      GCamera:MotionPhotoVersion="1"
      GCamera:MotionPhotoPresentationTimestampUs="0">
      <Container:Directory>
        <rdf:Seq>
          <rdf:li rdf:parseType="Resource">
            <Container:Item
              Item:Semantic="Primary"
              Item:Mime="image/jpeg"
              Item:Length="0"/>
          </rdf:li>
          <rdf:li rdf:parseType="Resource">
            <Container:Item
              Item:Semantic="MotionPhoto"
              Item:Mime="video/mp4"
              Item:Length="{mp4_size}"
              Item:Padding="0"/>
          </rdf:li>
        </rdf:Seq>
      </Container:Directory>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>"""

        # Write XMP using exiftool
        subprocess.run([
            'exiftool',
            '-overwrite_original',
            f'-xmp<={xmp_metadata}',
            output_path
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

        print("\n✅ Success! Motion Photo created:")
        print(f"  📂 Output: {os.path.basename(output_path)}")
        print(f"  📏 Total size: {get_file_size(output_path):,} bytes")
        print("\n👉 Transfer to Android device and open in Google Photos or Gallery app")
        print("   The photo will show a play icon to view the motion effect")

    except subprocess.CalledProcessError as e:
        print("❌ Error during processing:")
        if e.stderr:
            print(e.stderr.decode())
        else:
            print(str(e))
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        # Cleanup temp files
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print("🧹 Cleaned up temporary files")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 video_to_motion_photo.py <video_file> [output_path]")
        print("\nExample:")
        print("  python3 video_to_motion_photo.py myvideo.mp4")
        print("  python3 video_to_motion_photo.py myvideo.mp4 output_motion.jpg")
        sys.exit(1)

    video_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    check_dependencies()
    create_motion_photo(video_path, output_path)

if __name__ == "__main__":
    main()
