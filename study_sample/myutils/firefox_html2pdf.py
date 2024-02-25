import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


# 目前这个只能半自动
def convert(url, download_dir):
    # 设置Firefox下载路径及相关配置
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)  # custom location
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", download_dir)
    profile.set_preference("pdfjs.disabled", True)  # 禁用Firefox内置的PDF查看器
    profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
    profile.set_preference("print_printer", "Microsoft Print to PDF")  # 对于Windows系统，选择“Microsoft Print to PDF”
    profile.set_preference("print Preview.mode", "active")  # 这个设置可能帮助显示打印预览，可选
    profile.set_preference("print.always_print_silent", True)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # 下载文件类型
    # 配置Firefox浏览器为headless模式(如果需要的话)
    options = Options()
    options.headless = False
    # 创建一个新的Firefox浏览器实例
    driver = webdriver.Firefox(firefox_profile=profile, options=options)
    # 访问指定URL
    driver.get(url)

    js_height = "return document.body.clientHeight"
    k = 1
    try:
        # 模拟滚动至页面底部，触发懒加载
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.5)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        # 等待页面加载完成以及可能存在的懒加载内容
        wait = WebDriverWait(driver, 10)  # 可以根据实际情况调整超时时间
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))  # 确保主体元素加载
    except Exception as e:
        print(f"Error occurred while scrolling: {e}")
    # 等待一段时间确保所有异步内容加载完成
    # 使用Firefox的"Print to PDF"功能
#     driver.execute_script("""
#     window.onload = function() {
#         setTimeout(function() {
#             window.print();
#             setTimeout(function() {
#                 window.close();
#             }, 1000);
#         }, 500); // 等待页面稳定，防止打印过早
#     };
# """)
    # 模拟点击打印按钮并选择保存为PDF
    driver.execute_script("window.print();")
    # 关闭浏览器
    # driver.quit()


# 参见 puppeteer环境配置
# npm install puppeteer --ignore-scripts
def convertByJs(url, outpath):
    # 脚本路径
    script_path = 'puppeteer_print_pdf.js '

    args = [url, outpath]
    command = ['node', script_path] + args
    print(command)
    cmd = " ".join(command)
    print(cmd)
    # 创建子进程并执行Node.js命令
    process = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,  # 将字节流转换为文本流
                               encoding='utf-8')  # 指定输出的编码为UTF-8

    # 读取输出
    stdout, stderr = process.communicate()
    # 输出脚本执行的结果（标准输出和错误输出）
    print(stdout)
    print(stderr)

    # 检查返回码以确定脚本是否成功执行
    if process.returncode == 0:
        print("脚本成功执行")
    else:
        print("脚本执行失败")


if __name__ == '__main__':
    # 指定要下载PDF的目录
    download_dir = 'D:/test.pdf'
    url = 'https://mp.weixin.qq.com/s/JwbYMajRS4kMPx6Zc5Ng8A'
    # convert(url, download_dir)
    convertByJs(url, download_dir)

# 此时，PDF应该已经保存到了你之前指定的download_dir目录下