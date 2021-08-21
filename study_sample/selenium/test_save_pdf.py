import json
import logging
import os
import time
from selenium import webdriver

'''
本文件有问题.
'''

# settings = {
#     "appState": {
#         "recentDestinations": [
#             {
#                 "id": "Save as PDF",
#                 "origin": "local",
#                 "account": "",
#             }
#         ],
#         "selectedDestinationId": "Save as PDF",
#         "version": 2
#     }
# }
settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4"
    },
    "customMargins": {},
    "marginsType": 2,
    "isCssBackgroundEnabled": True
}
profile = {
    'printing.print_preview_sticky_settings': json.dumps(settings),
    'savefile.default_directory': './articles'
}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
# driver.implicitly_wait(60)
driver.implicitly_wait(5)

try:
    title = '测试保存pdf'
    url = 'https://mp.weixin.qq.com/s/JwbYMajRS4kMPx6Zc5Ng8A'
    driver.get(url)
    time.sleep(5)
    # 保存PDF
    temp_title = driver.title
    print(temp_title)
    driver.execute_script('document.title="'+temp_title+'";window.print();')
    time.sleep(10)
    # os.rename('./articles/' + temp_title + '.pdf', './articles/' + title + '.pdf')
except Exception as e:
    logging.exception(e)

driver.quit()
