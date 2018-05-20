# -*- coding: utf-8 -*-
# @Author: cyang812
# @Date:   2018-05-20 20:52:16
# @Last Modified by:   cyang812
# @Last Modified time: 2018-05-20 22:16:40

import sys
import threading
import serial
import time

import ctypes
import win32
import win32file
import win32con
import pywintypes

from PyQt5.QtWidgets import (QWidget, QPushButton, 
	QFrame, QApplication)
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
 
		# redb.clicked[bool].connect(self.open_close)
 
		saveToFileButton = QPushButton('saveOrNot', self)
		saveToFileButton.setCheckable(True)
		saveToFileButton.move(20, 60)
 
		saveToFileButton.clicked[bool].connect(self.open_close)
 
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
			
		if source.text() == 'openClose':
			if pressed == True:
				print('open uart')
				openCloseSerial()
			else:
				print('close uart')
		elif source.text() == 'Green':
			if pressed == True:
				print('g open')
			else:
				print('g close')                    

	def openCloseSerialProcess(self):
		try:
			if self.com.is_open:
				self.com.close()
				self.receiveProgressStop = True
				print('uart close')
				print('receiveCount =', receiveCount)
			else:
				try:
					self.com.baudrate = 9600
					self.com.port = 'COM3'
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

	def openCloseSerial(self):
		t = threading.Thread(target=self.openCloseSerialProcess)
		t.setDaemon(True)
		t.start()
		return              

	def receiveData(self):
		self.receiveProgressStop = False
		self.timeLastReceive = 0
		while(not self.receiveProgressStop):
			try:
				length = self.com.in_waiting # 错误，无句柄
				print(length)
				if length>0:
					content = self.com.read(length)
					self.receiveCount += len(content)
					# if self.receiveSettingsHex.isChecked():
					# 	strReceived = self.asciiB2HexString(content)
					# 	self.receiveUpdateSignal.emit(strReceived)
					# else:
					# 	self.receiveUpdateSignal.emit(content.decode(self.encodingCombobox.currentText(),"ignore"))
					# if self.receiveSettingsAutoLinefeed.isChecked():
					# 	if time.time() - self.timeLastReceive> int(self.receiveSettingsAutoLinefeedTime.text())/1000:
					# 		if self.sendSettingsCFLF.isChecked():
					# 			self.receiveUpdateSignal.emit("\r\n")
					# 		else:
					# 			self.receiveUpdateSignal.emit("\n")
					# 		self.timeLastReceive = time.time()
			except Exception as e:
				print("receiveData error")
				if self.com.is_open:
					self.com.close()
					# self.openCloseSerial()
					# self.detectSerialPort()
				print(e)
			time.sleep(0.009)
		return		

	   
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = uartToFile()
	sys.exit(app.exec_())