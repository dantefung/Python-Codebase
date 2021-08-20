import json
import logging
import os
import time
from selenium import webdriver


appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
profile = {
    'printing.print_preview_sticky_settings.appState': json.dumps(appState),
    'savefile.default_directory': './articles'
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(60)

try:
    title = '测试保存pdf'
    url = 'https://mp.weixin.qq.com/s/JwbYMajRS4kMPx6Zc5Ng8A'
    driver.get(url)
    time.sleep(5)
    # 保存PDF
    temp_title = driver.title
    driver.execute_script('window.print();')
    time.sleep(10)
    # os.rename('./articles/' + temp_title + '.pdf', './articles/' + title + '.pdf')
except Exception as e:
    logging.exception(e)

driver.quit()