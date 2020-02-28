# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以绑定任意属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):
    # 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
    age = 100
    def __init__(self, name):
        self.name = name

s = Student('Jack')
s.score = 90

print(s.age)
print(Student.age)
s.age = 900
print(s.age) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.age) # 但是类属性并未消失，用Student.name仍然可以访问
del s.age # 如果删除实例的name属性
print(s.age) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
r'''
从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
'''