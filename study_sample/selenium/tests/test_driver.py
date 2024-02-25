from selenium import webdriver

if __name__ == '__main__':
    # driver = webdriver.Chrome()    # Chrome浏览器
    # print(driver)

    # selenium3.141+geckodriver0.23.0 + firefox64
    firefox = webdriver.Firefox()
    print(firefox)

