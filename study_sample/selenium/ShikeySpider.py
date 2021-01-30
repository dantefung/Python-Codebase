from selenium import webdriver

FILEURLSLIST = []


def findAllLink(browser):
    # ----------------  FIND ALL LINK START -------------
    urls = browser.find_elements_by_xpath("//a")

    urlMetaData = []

    # collect meta data
    for url in urls:
        link = url.get_attribute("href")
        print(link)
        try:
            urlMetaObj = {"id":"", "name":"", "href":""}
            urlMetaObj['id'] = url.get_attribute("id")
            urlMetaObj['name'] = url.get_attribute("name")
            urlMetaObj['href'] = url.get_attribute("href")
            urlMetaData.append(urlMetaObj)
        except:
            pass

    print(urlMetaData)

    for metaObj in urlMetaData:
        if metaObj['id'] != '':
            print(metaObj['id'])
            url = browser.find_element_by_id(metaObj['id'])
            print(url)
            try:
                if url.get_attribute("name") == 'folderlist':
                    print('--Emm... FOLDER ~ open it!--')
                    url.click()
                    findAllLink(browser)
                    browser.back()
                elif url.get_attribute("name") == 'filelist':
                    print('--Emm... FILE ~ download it!--')
                    FILEURLSLIST.append(url.get_attribute("href").replace("?preview", ""))
            except:
                pass

    # ----------------  FIND ALL LINK END -------------


def out_put_link():
    fo = open("downloadlink.txt", "w")
    for link in FILEURLSLIST:
        fo.write(link+'\r\n')
    # 关闭打开的文件
    fo.close()





browser = webdriver.Chrome()
# 普通模式，会打开浏览器
# browser.get('https://d.shikey.com/')

# 2.1.2 Headless方式启动
r'''
Headless Chrome 是 Chrome 浏览器的无界面形态，可以在不打开浏览器的前提下，使用所有Chrome 支持的特性运行你的程序。
相比于现代浏览器，Headless Chrome 更加方便测试 web应用，获得网站截图, 做爬虫抓取信息等。
相比于较早的PhantomJS, SlimerJS等， Headless Chrome 则更加贴近浏览器环境。、

Headless Chrome 对Chrome版本要求：
官方文档中介绍，mac和linux环境要求chrome版本是59+，而windows版本的chrome要求是60+，同时chromedriver要求2.30+版本。

'''
# chrome_options = webdriver.ChromeOptions()
# # 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless') # 增加无界面选项
# chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
#
# # 启动浏览器，获取网页源代码
# browser = webdriver.Chrome(chrome_options=chrome_options)
# mainUrl = "https://d.shikey.com/"
# 算法训练营2020/
mainUrl = "https://d.shikey.com/%E6%9E%81%E5%AE%A2%E6%97%B6%E9%97%B4-%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A52020/"
#mainUrl = "https://d.shikey.com/%E6%9E%81%E5%AE%A2%E7%AE%97%E6%B3%95/"
browser.get(mainUrl)
# print(f"browser text = {browser.page_source}")

findAllLink(browser)
print('\r\n***********************\r\n\r\n', FILEURLSLIST, '\r\n\r\n**************************\r\n')

out_put_link()


# 通过name方式定位
# continue_link = browser.find_element_by_link_text('极客算法').click()
browser.quit()
