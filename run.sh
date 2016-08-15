#!/usr/bin/env bash
# input
dst_dir=./videos

# code
mkdir -p $dst_dir
python ./get_sicp_video_urls.py
aria2c -i ./sicp-video-urls.txt -d $dst_dir
