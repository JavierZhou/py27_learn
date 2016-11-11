#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

def isNum(sth):
    #sth = raw_input('请输入一些内容:')
    try:
        if type(int(sth)):
            print '这是纯数字'
    except ValueError:
        print '%s 不是纯数字' % sth



def fun(x, y):
    z = x + y
    return z



#isNum()

print fun(4, 6)