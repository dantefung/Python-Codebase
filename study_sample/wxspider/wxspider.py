import requests
from bs4 import BeautifulSoup
import webbrowser
import pdfkit

URL_LINK_LIST = []


def out_put_link():
    fo = open("article_links.txt", "w")
    for link in URL_LINK_LIST:
        fo.write(link + '\r\n')
    # 关闭打开的文件
    fo.close()


def write2disk(fileName, html):
    fo = open('.data/' + fileName + ".html", "w", encoding='UTF-8')
    fo.write(html)
    fo.close()

def get_page(url):
    try:
        # 需要加一个请求头部，不然会被网站封禁
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
        r = requests.get(url, headers=headers, timeout=10)
        return r.text
    except:
        return '发生异常'


htmlText = get_page('https://mp.weixin.qq.com/s/E7wNLtU-453b9YC3XoUvqQ')
print(htmlText)
# write2disk('路人甲Java之Spring系列', r.text)
soup = BeautifulSoup(htmlText, 'lxml')  # lxml为解析器

sortNo = 0
for item in soup.find_all('a'):
    if "mp.weixin.qq.com" in item.get('href'):
        print(item.get('href'), item.string)
        print(item.text)
        if "Spring" in item.text:
            r = requests.get(item.get('href'))
            write2disk(str(sortNo) + '-' + item.text, r.text)
            #fileName = str(sortNo) + '-' + item.text
            # pdfkit.from_url(item.get('href'), '.out/' + fileName + '.pdf')
        URL_LINK_LIST.append(item.get('href'))
        # webbrowser.open_new(item.get('href'))
    sortNo = sortNo + 1

out_put_link()

# pdfkit.from_url('http://google.com', 'out.pdf')
# pdfkit.from_file('test.html', 'out.pdf')
# pdfkit.from_string('Hello!', 'out.pdf')
# pdfkit.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
# pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')
# with open('file.html') as f:
#     pdfkit.from_file(f, 'out.pdf')
