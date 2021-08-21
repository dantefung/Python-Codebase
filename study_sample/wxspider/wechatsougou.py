from wechatsogou import *


# 获取公众号文章信息
from wechatsogou.five import readimg


def get_article(gzh):
    articles = ws_api.get_gzh_article_by_history(gzh)
    print(len(articles['article']))
    return articles['article']

def gzh_information(name):
    """
    功能: 获取公众号的基本信息
    :param name:公众号的名称
    :return:
    """
    wechats = WechatSogouAPI(captcha_break_time=1)
    wechat_infos = wechats.get_gzh_info(name)
    print(
        "名称:{}\n"
        "id:{}\n"
        "简介:{}\n"
        "最近一月群发数:{}\n".format(wechat_infos['wechat_name'],
                              wechat_infos['wechat_id'],
                              wechat_infos['introduction'],
                              wechat_infos['post_perm'],
                              )
    )


def get_gzh_article(name):
    """
    功能: 查找指定公众号的文章
    :param name:文章关键字
    :return:
    """
    wechats = WechatSogouAPI(captcha_break_time=1)
    data = wechats.get_gzh_article_by_history(name)
    print(data)


def identify_image_callback_by_hand(img):
    """识别二维码

    Parameters
    ----------
    img : bytes
        验证码图片二进制数据

    Returns
    -------
    str
        验证码文字
    """
    im = readimg(img)
    im.show()
    return input("please input code: ")

def search_gzh_article(name):
    """
        功能: 通过关键名字搜索相关文章
        :param name:文章关键字
        :return:
        """
    wechats = WechatSogouAPI(captcha_break_time=1)
    relate_article = wechats.search_article(name, page=1, identify_image_callback=identify_image_callback_by_hand)
    print(relate_article)
    for i in relate_article:
        print("来源公众号:{1}\t\t文章名称:{0}\t\t文章链接:{2}".format(i['article']['title'], i['gzh']['wechat_name'],
                                                         i['article']['url']))

def search_hot_article(type):
    """
          功能: 搜索热门相关文章
          :param name:
                       WechatSogouConst.hot_index.类别名
                例如:WechatSogouConst.hot_index.food
          :return:
          """
    wechats = WechatSogouAPI(captcha_break_time=1)
    relate_article = wechats.search_article(type)
    for i in relate_article:
        print(i['article'])
        print("来源公众号:{1}\t\t文章名称:{0}\t\t文章链接:{2}".format(i['article']['title'], i['gzh']['wechat_name'], i['article']['url']))


# 可配置参数

# 直连
ws_api = WechatSogouAPI()

# 验证码输入错误的重试次数，默认为1
# ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

# 所有requests库的参数都能在这用
# 如 配置代理，代理列表中至少需包含1个 HTTPS 协议的代理, 并确保代理可用
# ws_api = wechatsogou.WechatSogouAPI(proxies={
#     "http": "127.0.0.1:8888",
#     "https": "127.0.0.1:8888",
# })

# 如 设置超时
# ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)

# ws_api.get_gzh_info('南航青年志愿者')

gzh_list = ['全栈布道士', '编程人生', 'importNew', 'Python开发者', '非著名程序员',
                'Python之美', '机器学习研究会', '程序员大咖', '51CTO', '纯洁的微笑']
'''
pip install cachelib
修改filecache.py
# from werkzeug.contrib.cache import FileSystemCache
from cachelib import FileSystemCache
'''
# print(get_article('阁主早八点'))
# gzh_information('阁主早八点')
search_gzh_article('阁主早八点')