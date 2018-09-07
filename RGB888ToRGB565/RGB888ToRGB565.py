# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2018-09-07 13:06:04
# @Last Modified by:   cyang
# @Last Modified time: 2018-09-07 14:40:28

'''
/*
 * convert rgb888 to rgb565
 * color_src:     bmp[54], skip bmp header
 * color_src_len: height * width * 3
 * return:        height * width * 2
 */
uint32_t convertToRGB565(uint8_t *color_src, uint32_t color_src_len)
{
	uint16_t n565Color = 0;
	uint8_t r, g, b;
	uint32_t idx = 0;
	uint16_t *out_src = (uint16_t *)color_src; 

	for(uint32_t i = 0; i < color_src_len; i += 3)
	{
		r = color_src[i];
		g = color_src[i + 1];
		b = color_src[i + 2];
		
		n565Color = (uint16_t)((((uint32_t)(r) << 8) & 0xf800) |   
 	          		    	   (((uint32_t)(g) << 3) & 0x07E0) |  
	    	       				 (((uint32_t)(b) >> 3)));  

	    out_src[idx++] = n565Color; 	        
	}

	return idx - 1; 
}
'''

import os
import struct

def RGB888ToRGB565(in_file, out_file):
	# 1 open
	try:
		in_file  = open(IN_FILE, 'rb') 
	except Exception as e:
		print(e)
		return

	out_file = open(OUT_FILE, 'wb')
	in_size  = os.path.getsize(IN_FILE)

	# 2 convert
	while True:
		block = in_file.read(3)
		if block:
			r = block[0]
			g = block[1]
			b = block[2]

			h8 = (r & 0xf8) | (g & 0xe0) >> 5
			l8 = (g & 0x1c)<<3 | (b & 0xf8)>>3
			out_file.write(struct.pack('B', h8))
			out_file.write(struct.pack('B', l8))
		else:
			break

	# 3 close
	in_file.close()
	out_file.close()
	print('complete')

if __name__ == '__main__':
	IN_FILE = input(r'input the file name: ')
	OUT_FILE = '565_' + IN_FILE

	RGB888ToRGB565(IN_FILE, OUT_FILE)
	# os.system('pause')