import codecs
import os

from selenium import webdriver
import re



''' 
获取百度页面的所有a标签
'''
def getAllATag():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    source_code = driver.page_source
    print(source_code)

    urls = re.findall(r'<a.*?href=.*?<\/a>', source_code, re.I)
    for url in urls:
        print(url)
    driver.close()


''' 
获取百度页面的源码.
'''
def getBaiduSourceCode():
    # url = 'http://www.baidu.com'
    url = 'http://mp.weixin.qq.com/s?__biz=MzkxNzIzNDU2Mw==&mid=2247483983&idx=1&sn=d5d638670d2b0c28f9821fbdaadb4768&chksm=c142f4a3f6357db597e94ce3683fd06653cde023895a16dbcb3e6f5510f1d4094e0be5336f18#rd'
    driver = webdriver.Chrome()
    driver.get(url)
    # 网页源码
    page = driver.page_source
    print(page)
    save_html(page)
    # 关闭浏览器
    driver.close()

def save_html(html):
    sdir = '.out'
    os.makedirs(sdir, exist_ok=True)
    with codecs.open(os.path.join(sdir, 'index.html'), "w", 'utf-8') as f:
        f.write(html)
        f.flush()

if __name__ == '__main__':
    getBaiduSourceCode()