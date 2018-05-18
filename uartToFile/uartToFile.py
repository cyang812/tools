# -*- coding: utf-8 -*-
# @Author: cy101
# @Date:   2018-05-18 18:59:51
# @Last Modified by:   cy101
# @Last Modified time: 2018-05-18 21:20:07

import serial
import serial.tools.list_ports
import threading

COM_PORT = 'COM2'
BAUDRATE = 9600

def find_serial():
	plist = list(serial.tools.list_ports.comports())

	if len(plist) <= 0:
	    print("没有发现端口!")
	else:
	    plist_0 = list(plist[0])
	    serialName = plist_0[0]
	    serialFd = serial.Serial(serialName, 9600, timeout=60)
	    print("可用端口名>>>", serialFd.name)


def open_serial(com, baudrate):
	try:
		serialFd = serial.Serial(com, baudrate, timeout=60)
		return serialFd
	except Exception as e:
		print(e)

def send_serial(com, content):
	com.write(content.encode())

def receive_serial(com, count):
	return com.read(count)

def close_serial(com):
	com.close()

if __name__ == '__main__':
	# find_serial()
	serial_1 = open_serial(COM_PORT, BAUDRATE)
	send_serial(serial_1 ,'test')
	content = receive_serial(serial_1, 5)
	print("content: "+str(content))
	close_serial(serial_1)

