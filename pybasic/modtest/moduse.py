#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: zzshneuq
# Email: zzshneuq@163.com
# Created Time : 2019年06月02日 星期日 11时14分14秒
# File Name: moduse.py
# Description:
"""

from mod1 import function2

try:
	function2()
	function1()
except NameError:
	print 'NameError! Cannot use function1() without import it'
else:
   	print "Use function1() straightly" 

import mod1
print 'After import module mode1: '
mod1.function1()


