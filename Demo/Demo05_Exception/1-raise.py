#!/usr/bin/python
# -*- coding:utf-8 -*-

class CustonException(Exception):
    def __init__(self, length, atleast):
        super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('>')
        if len(s) < 3:
            # raise引发自定义异常
            raise CustonException(len(s), 3)
    except CustonException as result:
        print('CustomException: Length = %d AtLeast = %d'%(result.length, result.atleast))
    else:
        print('No Exception')

main()