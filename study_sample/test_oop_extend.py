#!/usr/bin/python
# -*- coding:UTF-8  -*-

'测试面向对象编程：继承'

__Author__ = 'DANTE FUNG'

# 导模块(python文件名)
from Animal import animal
from Animal import dog

# 未缩进的代码，在python文件被载入的时候自动执行

print('-----------------------------------------')
animal.run()
dog.run()

#print('animal is Animal?', isinstance(animal,Animal))
#print('dog is Animal?', isinstance(dog,Animal))
#print('dog is Dog?', isinstance(dog,Dog))








