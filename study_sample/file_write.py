
import cgi

'''
将html文件写入磁盘
'''
def write2disk(fileName, html):
    try:
        fo = open(fileName + ".html", "w", encoding='UTF-8')
        fo.write(html)
        fo.close()
    except Exception as e:
        print(fileName, e)

fileName = './【死磕 Spring】—— IoC 之解析 <bean> 标签：开启解析进程.html'
# 处理文件名中的转义字符
fileName = cgi.escape(fileName)

write2disk(fileName, 'xxx')