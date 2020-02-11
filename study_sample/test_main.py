#!/usr/bin/python
# -*- coding:UTF-8  -*-

#python test_main.py
#python test_main.py test1 test2
#
# __name__值变化： 
#文件被执行时，__name__的值为__main__
#文件(作为模块)被导入:__name__的值为 文件名（模块名）本例中值为 test_main
#

__author__ = 'DANTE FUNG'

import sys
def Fuc():
    print('hello')

# 每个文件（模块）都可以任意写一些没有缩进的代码，并且在载入时自动执行，为了区分主执行文件还是被调用的文件，Python引入了一个变量__name__
print('当文件test_main.py内置属性__name__此时为:'+__name__)


#其中if __name__=="__main__":这个程序块类似与Java和C语言的中main（主）函数
if __name__ == '__main__':
    if len(sys.argv) !=3 :
        print('Usage:python input_name output_name')
        exit(1)
    f_input = sys.argv[1]
    f_output = sys.argv[2]
    print(f_input)
    print(f_output)
    Fuc()
