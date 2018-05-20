# -*- coding: utf-8 -*-
# @Author: cy101
# @Date:   2018-05-18 18:59:51
# @Last Modified by:   cy101
# @Last Modified time: 2018-05-18 21:20:07

import serial
import serial.tools.list_ports
import threading
import time

COM_PORT = 'COM7'
BAUDRATE = 115200

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


'''
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay, counter, serial):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.counter = counter
        self.serial = serial
    def run(self):
        print ("开始线程：" + self.name)
        # print_time(self.name, self.delay, self.counter)
        receive_serial(serial, self.counter)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

serial = open_serial(COM_PORT, BAUDRATE)

# 创建新线程
thread1 = myThread(1, "Thread-1", 1, 10, serial)
# thread2 = myThread(2, "Thread-2", 2, 5)


# 开启新线程
thread1.start()
# thread2.start()
thread1.join()
# thread2.join()
print ("退出主线程")
'''


if __name__ == '__main__':
	# find_serial()
	serial_1 = open_serial(COM_PORT, BAUDRATE)
	# send_serial(serial_1 ,'test')
	content = list()
	time1 = int(time.time())
	while True:
		content.append(receive_serial(serial_1, 1))
		time2 = int(time.time())
		if time2 - time1 > 100:
			break

	print("content: "+str(content))
	close_serial(serial_1)

	with open('uart.txt', 'wb') as f:
		for x in content:
			f.write(x)