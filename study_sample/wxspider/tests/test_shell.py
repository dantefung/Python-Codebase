import os

def simple():
    r = os.system('ls -al')
    print(r)


def call_python_script():
    r = os.system('python3 test_reg.py')
    print(r)

def call_wxhub():
    r = os.system('cd .. && python3 wxhub.py -biz 狂人学堂 -pl 10')

def call_multi_cmd():
    # coding: UTF-8
    import subprocess

    # os.system('cmd1 && cmd2')
    cmd1 = "cd ../"
    cmd2 = "ls"
    cmd = cmd1 + " && " + cmd2

    # 如下两种都可以运行
    subprocess.Popen(cmd, shell=True)
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    # call_python_script()
    # call_wxhub()
    call_multi_cmd()
