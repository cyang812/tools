# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2020-09-13 10:44:28
# @Last Modified by:   cyang
# @Last Modified time: 2020-09-19 09:35:13

import os
import send2trash

SUFFIX = ('.torrent', '.txt', '.url', 'rar', '.jpg', '.mht', '.gif', '.png', '.mhtml', '.xltd')
PATH = 'x:\\download'

def deleteFile(path):
	for folderName, subFolders, fileNames in os.walk(path):
		print('\n-----------------------------------')
		print('The current folder is ' + folderName)
		# print(subFolders, fileNames)
		if not os.listdir(folderName):
			print(folderName + ' is an empty folder, remove it')	
			filePath = os.path.join(folderName)
			print('#send2trash#: ' + filePath)
			# send2trash.send2trash(filePath)

		for subFolder in subFolders:
			print('SUBFOLDER of ' + folderName + ': ' + subFolder)
		for fileName in fileNames:
			print('FILE INSIDE ' + folderName + ': ' + fileName)

			#remove file to trash if its suffix is one of SUFFIX 	
			if fileName.endswith(SUFFIX):
				filePath = os.path.join(folderName, fileName)
				print('#send2trash#: ' + filePath)
				# send2trash.send2trash(filePath)
			elif fileName.endswith('.mp4'):
				filePath = os.path.join(folderName, fileName)
				fileSize = os.path.getsize(filePath)
				fileSize = round(fileSize/float(1024*1024), 2)
				print('%s, %d MB' % (filePath, fileSize))

				# if fileSize < 100:
					# send2trash.send2trash(filePath)


if __name__ == '__main__':
	deleteFile(PATH)