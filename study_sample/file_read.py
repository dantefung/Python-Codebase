
def m1():
    r'''
    一、readline
    '''
    with open('Animal.py', 'rt', encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(line)
def m2():
    r'''
    二、readlines
    '''
    # 一次读取所有行
    # with open('Animal.py', 'rt', encoding='utf-8') as f:
    #     for line in f.readlines():
    #         print(line)

    # 一次读取批定行数
    with open('Animal.py', 'rt', encoding='utf-8') as f:
        while True:
            for line in f.readlines(1000):
                print(line)


def m3():
    '''
    三、直接for循环
    :return:
    '''
    # 逐行读取
    for line in open("Animal.py"):
        print(line)


def m4():
    r'''
    四、fileinput模块
    :return:
    '''
    import fileinput
    for line in fileinput.input('Animal.py'):
        print(line)

def m5():
    '''
    linecache
    :return:
    '''
    # 指定范围读取(行数)
    import linecache
    text = linecache.getline('Animal.py', 4)
    print(text)


m4()