# -*- coding: utf-8 -*-
# @Author: cyang	
# @Date:   2018-05-18 15:42:17
# @Last Modified by:   cy101
# @Last Modified time: 2018-05-18 15:49:59

import os

# IN_FILE = 'test.ncm'
# OUT_FILE = IN_FILE.split('.')[0]

def fileToC(in_file, out_file):
	# 1 head and open
	try:
		in_file  = open(IN_FILE, 'rb') 
	except Exception as e:
		print(e)
		return

	out_file = open(OUT_FILE+'.c', 'w')
	in_size  = os.path.getsize(IN_FILE)
	array_name = os.path.basename(OUT_FILE)
	out_file.write('const unsigned char %s[%d] = {\n    '%(array_name, in_size))

	# 2 content
	while True:
		block = in_file.read(1024)
		if block:
			for i in range(0, len(block)):
				out_file.write('0x%02x'%block[i]+', ')
				if not (i+1)%16:
					out_file.write('\n    ')
		else:
			break

	# 3 } and close
	in_file.close()
	out_file.write('\n}')
	out_file.close()
	print('complete')

if __name__ == '__main__':
	IN_FILE = input(r'input the file name: ')
	OUT_FILE = IN_FILE.split('.')[0]

	fileToC(IN_FILE, OUT_FILE)
	os.system('pause')