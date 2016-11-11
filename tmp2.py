#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def isNum(s):
    for i in s:
        if i in '1234567890':
            pass
        else:
            print '%s 不是数字' % s
            sys.exit()
    else:
        print '%s 是数字' % s

isNum(sys.argv[1])