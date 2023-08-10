import os



def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)

# 根据创建时间排序
def fileSortedByCTime(file_list):
    file_list = sorted(file_list, key=lambda x: os.path.getmtime(x))
    return file_list





#path = input('请输入文件路径(结尾加上/)：')
path = '/Users/admin/Documents/prj/develop/sites/www/static/tmp/'


# 获取该目录下所有文件，存入列表中
file_list = []
dir_list = []
# f = os.listdir(path)
get_file_path(path, file_list, dir_list)
file_list = fileSortedByCTime(file_list)
n = 0
for filePath in file_list:
    fileName = os.path.basename(filePath)
    # 设置旧文件名（就是路径+文件名）
    oldname = path + fileName

    # 设置新文件名
    newname = path + 'a' + str(n + 1) + '.pdf'

    # 用os模块中的rename方法对文件改名
    os.rename(oldname, newname)
    print(oldname, '======>', newname)

    n += 1