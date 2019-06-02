#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: zzshneuq
# Email: zzshneuq@163.com
# Created Time : 2019年06月02日 星期日 12时49分38秒
# File Name: functest.py
# Description:
"""

def positionpassing(a,b,c):
	return a*b+c

print('{}*{}+{} is {}.'.format(1,2,3,positionpassing(1,2,3)))
print '**********************************************************'

def keywordpassing(a,b,c):
	return a*b+c

print('{}*{}+{} is {}.'.format(2,6,3,keywordpassing(b=6,a=2,c=3)))
print '**********************************************************'

def defaultvalue(a,b,c=9):
	return a*b+c

print('{}*{}+{} is {}.'.format(2,6,3,keywordpassing(b=6,a=2,c=3)))
print '**********************************************************'

try:
# keywordpassing(b=6,a=2,3)
	print('{}*{}+{} is {}.'.format(2,6,3,keywordpassing(2,c=3,b=6)))
#	print('{}*{}+{} is {}.'.format(2,6,3,keywordpassing(b=6,a=2,3)))
except SyntaxError:
	print 'non-keyword arg after keyword arg'
	print '(keywordpassing(b=6,a=2,3)) is not right format' 
except:
	print('{}*{}+{} is {}.'.format(2,6,3,keywordpassing(2,c=3,b=6)))
	print '(keywordpassing(2,c=3,b=6)) is right format' 

print('{}*{}+{} is {}.'.format(1,2,9,defaultvalue(b=2,a=1,c=9)))
print '**********************************************************'
