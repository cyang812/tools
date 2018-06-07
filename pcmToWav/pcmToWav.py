# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2018-06-07 11:30:01
# @Last Modified by:   cyang
# @Last Modified time: 2018-06-07 14:43:23

import os
import wave

def pcmToWav(in_file, out_file):

	in_file = open(in_file, 'rb')
	out_file = wave.open(out_file, 'wb')

	out_file.setnchannels(int(input("plese input channels [1/2]: ")))
	out_file.setframerate(int(input("plese input samplerate [32000]: ")))
	out_file.setsampwidth(2) #16-bit
	out_file.writeframesraw(in_file.read())
		
	in_file.close()
	out_file.close()
	print('complete')

if __name__ == '__main__':
	IN_FILE = input(r'input the file name: ')
	OUT_FILE = IN_FILE.split('.')[0]+'.wav'

	pcmToWav(IN_FILE, OUT_FILE)
	os.system('pause')