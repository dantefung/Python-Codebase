## 基本概念
### Python模块
Python模块(Module)， 是一个Python文件，以.py结尾，包含了Python对象定义和Python语句。

模块让你能够有逻辑地组织你的Python代码段。

把相关的代码分配到一个模块里能让你的代码更好用，更易懂。

模块能定义函数，类和变量，模块里也能包含可执行的代码。

### Python包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的Python的应用环境。

简单来说，包就是文件夹，但该文件夹必须存在`__init__.py`文件，该文件的内容可以为空。

`__init__.py`用于标识当前文件夹是一个包。

### 应用
#### 导入同级目录文件
  如果需要引入同级目录下的文件，则可以采用import一个模块的形式，即可调用。
  
  考虑同一目录下的两个python文件，test.py需要调用surpport.py钟的函数,目录结构如下:

```  
  | -- test.py 
  | -- support.py
```  

  support.py中的代码如下:
```python
    def print_func(par):
        print('Hello:', par)
        return
```

  test.py调用的代码如下:
```python
    #!usr/bin/python
    #-*- config: UTF-8 -*-
    # 导入模块
    import support
    # 现在可以调用模块里包含的函数了
    support.print_func("Runoob")
```

#### 导入子目录文件
  如果需要引入子目录下的文件，则可以采用import一个包的形式，将子目录封装成包，即可调用。
  
  考虑一个在package_runoob目录下的runoob1.py、runoob2.py、__init__.py文件, test.py为测试调用包的代码，目录结构如下:
  
```python
    test.py
    package_runoob
    |--__init__.py
    |-- runoob1.py
    |-- runoob2.py
```
__init__.py可以是空文件。

test.py 调用代码如下：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
 
runoob1()
runoob2()
```
也可以采用：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
import package_runoob.runoob1
import package_runoob.runoob2
 
package_runoob.runoob1.runoob1()
package_runoob.runoob2.runoob2()
```
