import requests
from bs4 import BeautifulSoup
import webbrowser

URL_LINK_LIST = []

def out_put_link():
    fo = open("article_links.txt", "w")
    for link in URL_LINK_LIST:
        fo.write(link+'\r\n')
    # 关闭打开的文件
    fo.close()

r = requests.get('https://mp.weixin.qq.com/s/E7wNLtU-453b9YC3XoUvqQ')
soup = BeautifulSoup(r.text, 'lxml') #lxml为解析器


for item in soup.find_all('a'):
    if "mp.weixin.qq.com" in item.get('href'):
        print(item.get('href'), item.string)
        URL_LINK_LIST.append(item.get('href'))
        webbrowser.open_new(item.get('href'))

out_put_link()
