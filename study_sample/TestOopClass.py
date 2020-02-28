#!/usr/bin/python
# -*- coding:UTF-8  -*-

'a oop test'

__author__ = 'DANTE FUNG'

# 任何没有缩进的代码，在载入的时候自动执行
print('我是没有缩进的代码test_oop_class')
# 导入模块

# 全局变量定义

# 类定义
class TestOopClass(object):
    
    # 注意：特殊方法“__init__”前后分别有两个下划线！！！
    #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self,name,score):
         self.name = name
         self.score = score

# 函数定义
    def print_score(self):
        print('%s: %s' % (self.name,self.score))
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C' 
# 主函数(主程序)
if __name__ == '__main__':
    print('我是模块test_oop_class.py的主函数!!!')
    bart = TestOopClass('Bart Simpson', 59)

    lisa = TestOopClass('Lisa Simpson', 87)

    print('bart.name =', bart.name)
    print('bart.score =', bart.score)
    bart.print_score()

    print('grade of Bart:', bart.get_grade())
    print('grade of Lisa:', lisa.get_grade())




