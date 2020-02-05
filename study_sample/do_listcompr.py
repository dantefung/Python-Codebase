# 列表生成式即List Comprehensions, 是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(1, 11)))
# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 11)])
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方:
print([x * x for x in range(1, 11) if x % 2 == 0])
# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])
# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)
# 因此，列表生成式也可以使用两个变量来生成list：
print([k + '=' + v for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# isinstance
x = 'abc'
y = 123
print(isinstance(x, str))
print(isinstance(y, str))


