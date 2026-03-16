#!/bin/bash
cd workspace/workspace/video_final_test
ffmpeg -y -f concat -i concat.txt -i audio.wav -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest final_video.mp4
ls -lh final_video.mp4
