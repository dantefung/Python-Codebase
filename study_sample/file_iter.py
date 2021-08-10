import os
from string import Template

# for root,dirs,files in os.walk(r"E:\ebook\Redis核心技术与实战\html版本"):
#     for file in files:
#         #获取文件所属目录
#         print(root)
#         #获取文件路径
#         print(os.path.join(root,file))


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

if __name__ == "__main__":
    #根目录路径
    root_path = r"E:\ebook\Redis核心技术与实战\html版本"
    #用来存放所有的文件路径
    file_list = []
    #用来存放所有的目录路径
    dir_list = []
    get_file_path(root_path,file_list,dir_list)
    print(file_list)
    print(dir_list)
    filter_list = ['index.html', 'footer.html', 'leftmenu.html', 'main.html', 'top.html']
    for filePath in file_list:
        fileName = os.path.basename(filePath)
        if fileName not in filter_list:
            s = Template("<li><a href=\"$fileName\" target=\"main\"> $fileName </a></li>")
            finalText = s.substitute(fileName=fileName)
            print(finalText)