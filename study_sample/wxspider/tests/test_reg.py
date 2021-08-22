#encoding=utf-8
import re
data = '<a href="/5.mp3" singer="陈慧琳">记事本</a>'
regex = '<a.*?singer="(.*?)">(.*?)</a>'
print(re.match(regex,data,re.DOTALL).groups())