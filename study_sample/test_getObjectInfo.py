r'''
获取对象信息
1.使用type()
'''
print(type(123))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或类，也可以使用type()判断
print(type(abs))

from Animal import dog

print(dog)

print('-------基本类型判断-----------')
# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print('type(123)==type(456):', type(123) == type(456))
print('type(123) == int:', type(123) == int)
print('type(\'abc\') == type(\'123\'):', type('abc') == type('123'))
print('type(\'abc\') == str:', type('abc') == str)
print('type(\'abc\') == type(123):', type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
print('-----判断一个对象是否是函数-------')
import types


def fn():
    pass


print('type(fn)==types.FunctionType:', type(fn) == types.FunctionType)
print('type(abs)==types.BuiltinFunctionType:', type(abs) == types.BuiltinFunctionType)
print('type(lambda x: x)==types.LambdaType:', type(lambda x: x) == types.LambdaType)
print('type((x for x in range(10)))==types.GeneratorType:', type((x for x in range(10))) == types.GeneratorType)

print('----使用isinstance()--------')
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print('------使用dir()----------')
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
r'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
'''
print(len('ABC'))
print('ABC'.__len__())

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
print('----MyDog-------')


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))
print('ABC'.lower())

print('----MyObject------')


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print('hasattr(obj, \'x\'):', hasattr(obj, 'x'))
print(obj.x)
print('hasattr(obj, \'y\'):', hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print('设置属性值后，hasattr(obj, \'y\'):', hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
r'''
如果试图获取不存在的属性，会抛出AttributeError的错误：

>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'
'''

# 获取属性'z'，如果不存在，返回默认值404
print(getattr(obj, 'z', 404))
# 也可以获得对象的方法：
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())