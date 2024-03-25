#!/usr/bin/env python
# coding=utf-8
'''
Author: cy-asus cy950812@gmail.com
Date: 2023-12-21 17:04:13
LastEditors: cy-asus cy950812@gmail.com
LastEditTime: 2024-03-25 20:33:14
FilePath: _tools_moveFile_moveFile.py
Description:

Copyright (c) 2024 by cy-asus, All Rights Reserved.
'''
import os
import shutil

def copy_videos(source_folder, destination_folder, video_extensions=['.mp4', '.avi', '.mkv']):
    # 遍历源文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 检查文件扩展名是否为视频扩展名
            if any(file.lower().endswith(ext) for ext in video_extensions):
                source_path = os.path.join(root, file)
                # 构建目标路径
                destination_path = os.path.join(destination_folder, file)
                # 移动文件
                shutil.move(source_path, destination_path)
                # shutil.copy2(source_path, destination_path)
                print(f"已移动：{source_path} 到 {destination_path}")

# 替换以下路径为实际路径
source_folder = 'F:\\download\\abc'
destination_folder = 'F:\\1'

copy_videos(source_folder, destination_folder)
