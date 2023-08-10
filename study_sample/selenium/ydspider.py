import json
import os
import time
from selenium import webdriver
import cgi

# --------------------------------  函数定义  START -----------------------------

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


'''
保存整个网页为图片
'''
def webshot(driver, url,saveImgName):
    driver.maximize_window()
    # 返回网页的高度的js代码
    js_height = "return document.body.clientHeight"
    picname = saveImgName
    link = url
    # driver.get(link)
    try:
        driver.get(link)
        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.3)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        driver.get_screenshot_as_file(picname + ".png")

        print("Process {} get one pic !!!".format(os.getpid()))
        time.sleep(0.1)
        driver.back()
    except Exception as e:
        print(picname, e)
''' 
收集url元信息,转一下格式为 [{"name":"面试题", "href":"http://xxx.xxx.com"}]
'''
def collectUrlMetaData(urls):
    urlMetaData = []
    for url in urls:
        filters = ['http://xxx.xx.cn/',''
            ,'http://xx.xx.cn/index'
            ,'https://github.com/YunaiV/SpringBoot-Labs'
            ,'https://github.com/YunaiV/onemall'
            ,'https://github.com/YunaiV/ruoyi-vue-pro']
        link = url.get_attribute("href")
        print(link)
        try:
            if link != None and link not in filters:
                urlMetaObj = {"name":"", "href":""}
                urlMetaObj['name'] = url.text
                urlMetaObj['href'] = url.get_attribute("href")
                urlMetaData.append(urlMetaObj)
        except:
            pass
    urlMetaData = delRepeatData(urlMetaData)
    print(urlMetaData)
    return urlMetaData

'''
去除重复的数据
'''
def delRepeatData(urlMetaData):
    newUrlMetaData = []
    for o in urlMetaData:
        if o['name'] != '':
            newUrlMetaData.append(o)
    return newUrlMetaData
'''
数组去重
'''
def getNonRepeatList(data):
    return list(set(data))


# --------------------------------  函数定义  END -----------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)
# driver.implicitly_wait(60)
# driver = webdriver.Chrome()

baseUrl = 'http://svip.xxx.cn/xxx/xxx'
driver.get(baseUrl)


time.sleep(0.2)

# 输入用户名
username = driver.find_element_by_id('username')
username.send_keys('xxx')

# 输入密码
password = driver.find_element_by_id('password')
password.send_keys('xxxx')

# 点击登录
driver.find_element_by_xpath('/html/body/div[1]/form[1]/button').click()

# 写出index.html作为索引页
articleUrl = baseUrl
folder = './articles/'
fileName = folder+'index'
driver.get(articleUrl)
page = driver.page_source
print('开始将'+fileName+'写入磁盘...')
write2disk(fileName, page)

# 获取页面的所有a标签
urls = driver.find_elements_by_xpath("//a")
# 收集url的元信息
urlMetaData = collectUrlMetaData(urls)
# # 将网页保存成图片
# articleUrl = urlMetaData[0]['href']
# folder = './articles/'
# fileName = folder+urlMetaData[0]['name']
# webshot(driver, articleUrl, fileName)
# # 将网页html写入磁盘
# driver.get(articleUrl)
# page = driver.page_source
# print(page)
# write2disk(fileName, page)

for metaData in urlMetaData:
    articleUrl = metaData['href']
    folder = './articles/'
    fileName = folder+metaData['name']
    webshot(driver, articleUrl, fileName)
    # 将网页html写入磁盘
    driver.get(articleUrl)
    page = driver.page_source
    # print(page)
    print('开始将'+fileName+'写入磁盘...')
    fileName = cgi.escape(fileName)
    write2disk(fileName, page)





