#!/bin/bash
cd workspace/workspace/video_final_test
ffmpeg -y -loop 1 -i frame_0.jpg -c:v libx264 -t 2.5 -pix_fmt yuv420p -r 25 part_0.mp4
ffmpeg -y -loop 1 -i frame_1.jpg -c:v libx264 -t 4.0 -pix_fmt yuv420p -r 25 part_1.mp4
ffmpeg -y -loop 1 -i frame_2.jpg -c:v libx264 -t 3.5 -pix_fmt yuv420p -r 25 part_2.mp4
ffmpeg -y -loop 1 -i frame_3.jpg -c:v libx264 -t 5.0 -pix_fmt yuv420p -r 25 part_3.mp4
ffmpeg -y -f concat -i concat_vid.txt -c copy merged_video.mp4
ffmpeg -y -i merged_video.mp4 -i audio.wav -c:v copy -c:a aac -shortest final_video.mp4
ls -lh final_video.mp4
