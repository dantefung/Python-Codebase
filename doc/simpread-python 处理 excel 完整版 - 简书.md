> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.jianshu.com](https://www.jianshu.com/p/90569d5044be)

openpyxl 的用法实例
==============

#### 1.1 Openpyxl 库的安装使用

> openpyxl 模块是一个读写 Excel 2010 文档的 Python 库，如果要处理更早格式的 Excel 文 档，需要用到额外的库，openpyxl 是一个比较综合的工具，能够同时读取和修改 Excel 文档。 其他很多的与 Excel 相关的项目基本只支持读或者写 Excel 一种功能。新建、读取、保存工 作簿。

``` 
pip install Openpyxl
```

#### 1.2 Excel 的新建、读取、保存

**1.2.1 新建保存工作簿 (覆盖创建）

> 新建：openpyxl.Workbook()，注意这个的 W 是大写的（本人吃过亏），可以设置 write_only=True/False 的读写方式，默认是可写。 保存：workbook.save('工作簿名. xlsx')

```
from openpyxl import Workbook
wb=Workbook() # 新建工作簿
 wb.save('我的工作簿.xlsx') # 相对路径保存工作簿
```

> 每个 workbook 创建后，默认会存在一个 sheet。也可以自行创建新的 sheet。

###### 1.2.2 读取保存工作簿

> 读取工作簿：  
> openpyxl.load_workbook('工作簿名. xlsx')，注意以下相关参数的设置。  
> read_only=False/True False 表示可以读、写，True 表示只能读、不能写。  
> guess_types=False/True False 表示转换数据，True 表示不能转换数据。  
> data_only=False/True False 表示序单元格的真实信息，True 表示只读取值。

```
1-> from openpyxl import load_workbook
 2-> wb=load_workbook('成绩表-1.xlsx') # 读取 工作簿
 3-> wb.save('成绩表-2.xlsx') # 保 存工作簿
```

> 1.2.3 实例（批量建新工作簿）

```
1-> from openpyxl import Workbook 
 2-> for m in range(1,13): 
 3->     wb = Workbook()  # 新建工作簿
 4->     wb.save('%d 月.xlsx'%m)# 保存工作簿
```

#### 1.3 工作表对象的获取方法

###### 1.3.1 工作表获取方式:

获取当前活动工作表的：

```
sheet = wb.active
```

以索引值方式获取工作表：

```
sheet= wb.worksheets[2]
```

以工作表名获取： wb['工作表名']，注意，此表达方式为切片显示，所以没有成员提示。很少用

```
sheet = wb["Sheet-甲乙-甲乙"]
```

循环工作表：很好用，一般用 sheetnames

```
wb = wb .worksheets
```

获取所有工作表名：wb.sheetnames

```
wb4 = wb.sheetnames
```

获取指定工作表名

```
wb7 = wb.sheetnames[2].title()
```

修改工作表名称

###### 1.3.2 实例（批量修改工作表名）

#### 1.4 工作表的新建、复制、删除

###### 1.4.1 新建工作表

> 可以在新建的工作簿中新建工作表（在新建工作簿时，会默认新建一个工作表）。也能在已经存在的工作簿中新建工作表。

_新建工作表时的默认工作表名：_

```
1-> import openpyxl 
2-> wb=openpyxl.load_workbook('各年业绩表.xlsx') 
3-> for sh in wb.worksheets:
4->     sh.title=sh.title+'-芝华公司'
5-> wb.save('各年业绩表（修改后）.xlsx')
```

```
wb.create_sheet()  #默认工作表名为 Sheet1、 Sheet2、 Sheet3……
```

###### 1.4.2 复制工作表

```
wb8 = wb.create_sheet('工作表名',指定位置)
```

###### 1.4.3 删除工作表

workbook.remove(工作表)

```
wb.copy_worksheet(wb.worksheets[3])
```

1.5 关于工作表的实例应用
==============

##### 1.5.1 实例应用（批量新建 12 个月工作表）

```
wb.remove(wb.worksheets[2])
```

###### 1.5.2 实例应用（删除不符合条件的工作表）

```
import openpyxl
wb = openpyxl.Workbook()  # 新建工作簿
for m in range(1, 13):
     wb.create_sheet('%d 月' % m)  # 新建月份工作表
wb.remove(wb['Sheet'])  # 删除 指定工作表
wb.save('2019 年计划表.xlsx')  # 保存工作簿。
```

###### 1.5.3 实例应用（批量复制工作表）

```
import openpyxl 
wb=openpyxl.load_workbook('2018 年.xlsx')  # 读取 工作簿
for sh in wb: # 循环 工作簿中的工作表
    if sh.title.split('-')[0]!='北京': # 判断 工作表是否不等于北京
          wb.remove(sh) # 删除 工作表
wb.save('北京.xlsx') # 保 存工作簿
```

以上是处理工作表的方式
===========

> * * *

以下是处理单元格的方法
===========

#### 1.6 单元格信息获取

###### 1.6.1 单元格数据获取

A1 表示法：_工作表 ['A1']_，R1C1 表示法：工作表. cell(行号, 列号)

```
import openpyxl

wb = openpyxl.load_workbook('模板.xlsx')
for m in range(1, 13):
    wb.copy_worksheet(wb['测试']).title = '%d 月' % m
    wb.remove(wb['测试'])

wb.save('2018 年各月表格.xlsx')
```

###### 1.6.2 实例应用（汇总各表各单元格数据）

```
import openpyxl

wb = openpyxl.load_workbook("测试表格.xlsx")

ws = wb.worksheets[0] #不能使sheetnames
sh2 = ws["a1"].value #必须是小写
sh = ws.cell(1,1).value
print(type(sh2))

wb.save("测试表格.xlsx")
```

#### 1.7 单元格区域信息获取

###### 1.7.1 单元格区域数据获取

> 1. 工作表 ['起始单元格': '终止单元格'] 或工作表['起始单元格: 终止单元格']，此方法是按行读取的数据。

```
import openpyxl
wb = openpyxl.load_workbook('各年业绩表.xlsx')
print(sum([s['b14'].value for s in wb]))
print(sum([s.cell(14,2).value for s in wb]))
```

2. 工作表 ['起始行号': '结束行号'] 或者工作表['起始行号: 结束行号']，此方法是按行读取的数据。

```
import openpyxl
wb = openpyxl.load_workbook('demo.xlsx')
sh = wb["天峰集团"]
s = sh["a1":"a2"]
print(s)
wb.save("demo.xlsx")
```

3. 工作表 ['起始列号': '结束列号'] 或者工作表['起始列号: 结束列号']，  
此方法是按列读取的数据。

```
import openpyxl
wb = openpyxl.load_workbook('demo.xlsx')
sh = wb["天峰集团"]
s = sh["1:3"]
print(s)
wb.save("demo.xlsx")
```

4. 获取（按行）指定工作表所有已用数据：  
list(workbook.worksheets[索引值].values)

```
import openpyxl
wb = openpyxl.load_workbook('demo.xlsx')
sh = wb["天峰集团"]
s = sh["a:w"]
print(s)
wb.save("demo.xlsx")
```

#### 1.7.2 实例应用

按行求和（方法 1）

```
print([[c.value for c in row] for row in ws['a1:d3']])
```

按行求和（方法 ）

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.active
rngs=ws['a2:e71']
print(['%s-%d'%(row[0].value,sum([c.value for c in row][1:])) for row in rngs])
```

按列统计平均值

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.active
print(['%s-%d'%(row[0],sum(row[1:])) for row in list(ws.values)[1:]])
```

#### 1.8 行列信息获取

###### 1.8.1 行列信息获取

按行获取工作表使用区域数据：worksheet.rows

按列获取工作表使用区域数据：worksheet.columns  
获取工作表中最小行号：worksheet.min_row  
获取工作表中最小列号：worksheet.min_column  
获取工作表中最大行号：worksheet.max_row  
获取工作表中最大列号：worksheet.max_column  
获取单元格的行号：cell.row  
获取单元格的列号：cell.column iter  
方法获取指定区域：  
1. 按行获取指定工作表单元格区域：worksheet.iter_rows(……)  
2. 按列获取指定工作表单元格区域：worksheet.iter_cols(……)  
可以通过 min_row、min_col、max_col、max_row 这几个参数进行单元格区域的控制

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.active

f=[sum(l)/len(l) for l in list(zip(*list(ws.values)[1:]))[1:]]
n=[c.value for c in ws['1']][1:]
print(['%s-%.2f'%c for c in list(zip(n,f))])

print(['%s-%.2f'%(l[0],sum(l[1:])/len(l[1:])) for l in list(zip(*list(ws.values)))[1:]])
```

#### 1.8.2 实例应用

```
import openpyxl
wb=openpyxl.load_workbook('demo.xlsx')
ws=wb.active
minr=ws.min_row
minc=ws.min_column
maxr=ws.max_row
maxc=ws.max_column
rngs=ws.iter_rows(min_row=minr+1,min_col=minc+2,max_row=maxr-1,max_col=maxc-1)
col=ws.iter_cols(min_row=minr+1,min_col=minc+1,max_row=maxr-1,max_col=minc+1)
total=([sum([v.value for v in row]) for row in rngs])
cp=([[v.value for v in row] for row in col][0])
print(list(zip(cp,total)))
```

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
for row in ws.iter_rows(min_row=36,min_col=2,max_col=4,max_row=40):
    print([c.value for c in row])
```

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
for row in list(ws.rows)[1:]:
    l=[v.value for v in row]
    print(l[0],sum(l[1:]))
```

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
for col in list(ws.columns)[1:]:
    l=[v.value for v in col]
    print(l[0],max(l[1:]))
```

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
total=[sum([c.value for c in row]) for row in ws.iter_rows(min_col=2,min_row=2)]
name=[c.value for c in ws['a']][1:]
print(list(zip(name,total)))
```

单元格的写入
======

###### 1.9.1 单元格与区域数据写入

A1 表示法：工作表 ['A1']= 值，R1C1 表示法：工作表. cell(行号, 列号, 值)

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
total=[sum([c.value for c in col]) for col in ws.iter_cols(min_col=2,min_row=2)]
name=[c.value for c in ws[1][1:]]
print(list(zip(name,total)))
```

###### 1.9.2 实例应用（九九乘法表）

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[1]
s = ws['a1']=123
ws.cell(2,3,'我是中国人')
ws.cell(3,3).value='我是四川人'
print(s)
wb.save('test.xlsx')
```

#### 1.10 批量写入数据

###### 1.10.1 按行写入数据 (追加)

在最后一行写入数据：工作表. append(列表)

```
import openpyxl
wb=openpyxl.Workbook()
ws=wb.active
ws.title='九九表'
for x in range(1,10):
    for y in range(1,x+1):
        ws.cell(x,y,f'{y}×{x}={x*y}')
wb.save('九九表.xlsx')
```

1.10.2 实例应用（九九乘法表）

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
ws.append({'a':'张三','b':56,'c':'fdgsfg'})
wb.save('test.xlsx')
```

#### 1.11 循环方式批量写入数据

###### 1.11.1 循环获取单元格对象，再写入

> 之前我们可以通过组合单元格来获取或者写入数据，但还有一种方法，就是直接循环单 元格区域来写入数据。与循环读取的表示方式基本相同，只是多了一个赋值。

```
wb=openpyxl.load_workbook('demo.xlsx')
ws=wb.active
# for r in [['%d*%d=%d'%(y,x,x*y) for y in range(1,x+1)] for x in range(1,10)]:
#     ws.append(r)
# ws.delete_rows(1)
# wb.save('demo.xlsx')
for row in ws['a1:c6']:
    for c in row:
        c.value=1
wb.save('demo.xlsx')
```

###### 1.11.2 实例应用（大于等于 90 分为优秀）

```
import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.worksheets[0]
for row in ws['a1:g9']:
    print(row)
    for c in row:
        print(c.value)
wb.save('test.xlsx')
```

###### 1.11.3 实例应用（每个人的总分大于等于 300 为优秀）

最后加一列写优秀

```
import openpyxl
wb=openpyxl.load_workbook('demo.xlsx')
ws=wb.active
rngs=ws.row("2:2")
for row in rngs:
    for c in row:
        if c.value>=90:
            c.value=str(c.value)+'（优秀）'
wb.save('demo1.xlsx')
```