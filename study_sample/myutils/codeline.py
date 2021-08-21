#! python
# coding: utf-8
import os
import sys

## 统计某个文件夹下面的python脚本文件的代码行数.

l = []
for path, dirs, fns in os.walk('../enchance_oop'):
    for fn in fns:
        if fn.endswith('.py'):
            fn = os.path.join(path, fn)
            fp = open(fn)
            l.append((len(fp.readlines()), fn))

l.sort(reverse=True)
for lines, path in l:
    print(lines, path)
sys.stdout.close()