import pdfkit

pdfkit.from_file('test.html', '.out/out.pdf')
pdfkit.from_url('www.baidu.com', '.out/baidu.pdf')
pdfkit.from_url("https://mp.weixin.qq.com/s?__biz=MzA5MTkxMDQ4MQ==&mid=2648933921&idx=1&sn=db7ff07c5d60283b456fb9cd2a60f960&chksm=88621e1fbf15970919e82f059815714545806dc7ca1c48ed7a609bc4d90c1f4bb52dfa0706d5&token=157089977&lang=zh_CN&scene=21#wechat_redirect"
,'.out/test.pdf')