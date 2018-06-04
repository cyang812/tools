# -*- coding: utf-8 -*-
# @Author: cyang812
# @Date:   2018-05-20 20:52:16
# @Last Modified by:   cyang
# @Last Modified time: 2018-06-04 18:32:06

import sys
import threading
import serial
import time

import ctypes
import win32
import win32file
import win32con
import pywintypes

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor

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

class uartToFile(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		self.com = serial.Serial()
		
	def initUI(self):      
 
		self.col = QColor(0, 0, 0)       
 
		serialOpenCloseButton = QPushButton('openClose', self)
		serialOpenCloseButton.clicked.connect(self.openCloseSerial)
		serialOpenCloseButton.setCheckable(True)
		serialOpenCloseButton.move(20, 10)
 
		saveToFileButton = QPushButton('saveOrNot', self)
		saveToFileButton.clicked[bool].connect(self.open_close)
		saveToFileButton.setCheckable(True)
		saveToFileButton.move(20, 60)
 
		self.square = QFrame(self)
		self.square.setGeometry(150, 20, 100, 100)
		self.square.setStyleSheet("QWidget { background-color: %s }" %  
			self.col.name())
		
		self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle('uart To File')
		self.show()
		
	def open_close(self, pressed):
		
		source = self.sender()
		print(source.text(), pressed)
			
		if source.text() == 'saveOrNot':
			if pressed == True:
				print('save file')
			else:
				print('close file')

	def openCloseSerial(self):
		print('openCloseSerial')
		t = threading.Thread(target=self.openCloseSerialProcess)
		t.setDaemon(True)
		t.start()
		return 

	def openCloseSerialProcess(self):
		try:
			if self.com.is_open:
				self.com.close()
				self.receiveProgressStop = True
				print('uart close')
				print('receiveCount =', self.receiveCount)
			else:
				try:
					self.com.baudrate = 115200
					self.com.port = 'COM7'
					print(self.com)
					self.com.open()
					print('uart open')
					receiveProcess = threading.Thread(target=self.receiveData)
					receiveProcess.setDaemon(True)
					receiveProcess.start()
				except Exception as e:
					self.com.close()
					print('uart open fail')
					print(e)
					self.receiveProgressStop = True
		except Exception as e:
			print(e)
		return              

	def receiveData(self):
		self.receiveProgressStop = False
		self.receiveCount = 0
		self.timeLastReceive = 0
		while(not self.receiveProgressStop):
			try:
				if self.com.is_open:
					print("is_open")
					content = self.com.read(1)
					print("try read")
					if len(content):
						self.receiveCount += len(content)
						print("content = ", content)
			except Exception as e:
				print(e)
				print("receiveData error")
				if self.com.is_open:
					print("self.com.close")
					self.com.close()
		return		
	   
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = uartToFile()
	sys.exit(app.exec_())