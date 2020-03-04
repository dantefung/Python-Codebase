# 使用枚举类

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份:

'''

JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
'''

# 好处是简单，缺点是类型是int,并且仍然是变量。

# 更好的方法是为这样的枚举类定义一个class类型，然后，每个常量都是class的一个唯一实例。

# Python提供了Enum类来实现这个功能:

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 这样我们就获得Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''
控制台输出:
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
'''

# value属性则是自动赋给成员的int变量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类:
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique装饰器可以帮助我们能检查保证没有重复值
# 访问这些枚举类型可以有若干种方法:
day1 = Weekday.Mon
print(day1) # 输出Weekday.Mon
print(Weekday.Tue) # 输出Weekday.Tue
print(Weekday['Tue']) # 输出Weekday.Tue
print(Weekday.Tue.value) # 输出2
print(day1 == Weekday.Mon) # 输出 True
print(day1 == Weekday.Tue) # 输出 False
print(Weekday(1)) # Weekday.Mon
print(day1 == Weekday(1)) # True
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
r'''
输出:
Sun => Weekday.Sun
Mon => Weekday.Mon
Tue => Weekday.Tue
Wed => Weekday.Wed
Thu => Weekday.Thu
Fri => Weekday.Fri
Sat => Weekday.Sat

'''

'''
可见
1.索引  --> 引用枚举常量
2.成员名称 --> 引用枚举常量
3.value  --> 取得枚举常量值
'''




