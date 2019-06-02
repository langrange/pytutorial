#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: zzshneuq
# Email: zzshneuq@163.com
# Created Time : 2019年06月02日 星期日 11时43分56秒
# File Name: itetest.py
# Description:
"""

re = iter(range(5))
try:
	for i in range(100):
		   	print re.next()
except StopIteration:
	   	print 'here is end '
	   	print 'HaHaHaHa'
else:
		print 'go straight'
