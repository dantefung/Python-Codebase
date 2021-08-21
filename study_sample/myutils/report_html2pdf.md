
使用 Selenium 调用 Chromium 浏览器的无头模式，将打开的 HTML 打印导出为 PDF，算是比较完美地解决了觅道文档中文集导出 PDF 的问题。下面来看看最核心的实现过程：

依赖库
---

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import base64
```

配置 chrome 的启动参数
---------------

```
webdriver_options = Options()
webdriver_prefs = {}

webdriver_options.add_argument('--headless')
webdriver_options.add_argument('--disable-gpu')
webdriver_options.add_argument('--no-sandbox')
webdriver_options.add_argument('--disable-dev-shm-usage')
webdriver_options.experimental_options['prefs'] = webdriver_prefs
webdriver_prefs['profile.default_content_settings'] = {'images': 2}
```

实例化一个 Chrome
------------

首先在 Selenium 中 实例化一个 Chrome 对象：

```
driver = webdriver.Chrome(executable_path=settings.CHROMIUM_DRIVER_PATH,options=webdriver_options)
```

然后请求 HTML 文件，`path` 为 HTML 文件路径，也可以为 url：

```
driver.get(path)
```

加载及处理
-----

首先等待请求加载的完成：

```
WebDriverWait(driver, timeout).until(staleness_of(driver.find_element_by_tag_name('html')))
```

然后，配置一个用于打印命令的字典：

```
calculated_print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True,
        }
```

接着，获取 selenium 当前 session 的相关信息，使用让 Chrome 执行 `Page.printToPDF` 这一用于打印页面的命令：

```
resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': 'Page.printToPDF', 'params': calculated_print_options })
    response = driver.command_executor._request('POST', url, body)
```

获取到最后的响应：

```
result = response.get('value')
```

最后将响应写入文件之中：

```
with open('report.pdf', 'wb') as file:
    file.write(result)
```

这样，就实现了 HTML 到 PDF 文件的转换。

模块调用
----

实际上，Pypi 中已经存在第三方模块实现了上述的流程，并且添加了 PDF 文件压缩的功能。通过如下命令即可安装使用：

```
pip install pyhtml2pdf
```

具体的使用方法详见：https://pypi.org/project/pyhtml2pdf/

上述实现的觅道文档代码位于：https://gitee.com/zmister/MrDoc/blob/master/app_doc/report_html2pdf.py