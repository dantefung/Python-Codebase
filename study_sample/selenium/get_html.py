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
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    # 网页源码
    page = driver.page_source
    print(page)
    # 关闭浏览器
    driver.close()


getAllATag()