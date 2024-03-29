#!/usr/bin/python

import sqlite3

# 测试连接数据库
def connect_db():
    conn = sqlite3.connect('test.db')
    print("Opened database Successfully!")


# 测试创建表
def create_table():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print("Table created successfully")
    conn.commit()
    conn.close()

# 测试插入语句
def insert():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print("Records created successfully")
    conn.close() 

def select():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")

    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print
        "ID = ", row[0]
        print
        "NAME = ", row[1]
        print
        "ADDRESS = ", row[2]
        print
        "SALARY = ", row[3], "\n"

    print("Operation done successfully")
    conn.close()

def update():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print
    "Opened database successfully"

    c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()

if __name__ == '__main__':

    # 测试数据库连接
    connect_db()
    # 测试创建表
    # create_table()
    # 测试插入语句
    # insert()
    # 测试查询
    select()
    # 测试更新
    update()

    

