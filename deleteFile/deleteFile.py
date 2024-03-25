# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2020-09-13 10:44:28
# @Last Modified by:   cyang
# @Last Modified time: 2023-11-25 15:28:56

import os
import send2trash
from moviepy.editor import VideoFileClip

SUFFIX = ('.txt', '.jpg', '.rar')
PATH = 'F:\download'

def deleteFile(path):
    for folderName, subFolders, fileNames in os.walk(path):
        print('\n-----------------------------------')
        #print('The current folder is ' + folderName)
        # print(subFolders, fileNames)
        if not os.listdir(folderName):
            #print(folderName + ' is an empty folder, remove it')
            filePath = os.path.join(folderName)
            delete(filePath, 'dir')

        #for subFolder in subFolders:
            #print('SUBFOLDER of ' + folderName + ': ' + subFolder)
        for fileName in fileNames:
            # print('FILE INSIDE ' + folderName + ': ' + fileName)

            #remove file to trash if its suffix is one of SUFFIX
            if fileName.endswith(SUFFIX):
                filePath = os.path.join(folderName, fileName)
                delete(filePath, fileName.split('.')[-1])
            elif fileName.endswith('.mp4'):
                filePath = os.path.join(folderName, fileName)
                fileSize = os.path.getsize(filePath)
                fileSize = round(fileSize/float(1024*1024), 2)
                #print('%s, %d MB' % (filePath, fileSize))

                if fileSize > 20000000:
                    delete(filePath, str(fileSize) + 'MB')
                else:
                    duration = getVideoInfo(filePath)
                    if duration > 300000:
                        delete(filePath, str(fileSize) + 'MB' + ' | ' + f"{duration:.2f}" + 's')

def delete(filePath, type):
    print('#send2trash# %15s | %s' % (type, filePath))
    send2trash.send2trash(filePath)

def getVideoInfo(file_path):
    try:
        # 打开视频文件
        video_clip = VideoFileClip(file_path)

        # 获取视频时长
        duration = video_clip.duration

        # 获取视频帧数
        frames = video_clip.fps * duration

        # 获取视频分辨率
        resolution = video_clip.size

        # 输出视频信息
        print(f"视频时长: {duration} 秒")
        # print(f"视频帧数: {frames} 帧")
        # print(f"视频分辨率: {resolution[0]} x {resolution[1]} 像素")

        return duration

    except Exception as e:
        print(f"发生错误: {str(e)}")

    finally:
        # 在 finally 块中调用 close() 方法确保资源的释放
        if video_clip:
            video_clip.close()

if __name__ == '__main__':
    deleteFile(PATH)