class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果

s2 = Student()  # 创建新的实例
# s2.set_age(25) # 尝试调用方法
r'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'set_age'
'''


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

print('---------使用slots----------')
r'''
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
'''
class Teacher(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
t = Teacher() # 创建新的实例
t.name = 'Michael' # 绑定属性'name'
t.age = 25 # 绑定属性'age'
#t.score = 99 # 绑定属性'score'
r'''
Traceback (most recent call last):
  File "enhance_oop_slots.py", line 50, in <module>
    t.score = 99 # 绑定属性'score'
AttributeError: 'Teacher' object has no attribute 'score'
'''
r'''
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
class GraduateTeacher(Teacher):
    pass
g = GraduateTeacher()
g.score = 9999
print(g.score)

