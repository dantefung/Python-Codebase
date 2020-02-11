#!/usr/bin/python
# -*- coding:UTF-8  -*-
import os

# 方式一: 通过OS模块判断文件是否存在
# 判断文件是否存在
print(os.path.exists('config_parser.ini'))
# 判断文件夹是否存在
print(os.path.exists('test_dir'))
# 检查文件
print(os.path.isfile('config_parser.ini'))
# 判断文件是否可做读写操作
# 语法糖: os.access(path,mode)
if os.access('config_parser.ini',os.F_OK):
    print('Given file path is exist!')
if os.access("config_parser.ini", os.R_OK):
    print("File is accessible to read")

if os.access("/Users/admin/Documents/script/exercise/python/config_parser.ini", os.W_OK):
    print("File is accessible to write")

if os.access("config_parser.ini", os.X_OK):
    print("File is accessible to execute")

# 方式二: 通过Try语句

# 方式三:使用pathlib模块(Python3中内置的模块)
