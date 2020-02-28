#!/usr/bin/python
# -*- coding:UTF-8  -*-

# 头部描述
'student class'

# 全局变量定义
__author__ = 'DANTE FUNG'

# 类定义
class Student(object):

    # __开头的属性都是私有的
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            return ValueError('bad score')


# 函数定义


# 主函数



# 未缩进的代码，载入时自动执行
stu = Student('zhangsan',90)
stu.print_score()
stu.set_score(30)
stu.print_score()
stu.set_name('lisa')
stu.print_score()

    

