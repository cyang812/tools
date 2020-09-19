# -*- coding: utf-8 -*-
# @Author: cyang
# @Date:   2020-09-13 21:26:06
# @Last Modified by:   cyang
# @Last Modified time: 2020-09-13 21:29:06

import time

def calcProd():
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product	


startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))