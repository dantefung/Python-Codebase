#!/usr/bin/python
# vim: set fineecoding=utf-8
print('Hello World!')

####################################
# learn to fail, failure to learn！
# AUTHOR:DANTE FUNG
###################################

#import ConfigParser
#
#cf=ConfigParser.ConfigParser()
# 读取配置文件(ini、conf)返回结果列表
# cf.read("./config_parser.ini")
# 获取到的所有sections(域)，返回列表类型
# cf.sections()
# 某域下的所有key，返回列表类型
# cf.options('sectionname')
# 某域下的所有key,value对
# cf.items('sectionname')
# 获取某个域下的key对应的value值
# value=cf.get('sectionname','key')
# 获取的value值的类型
# cf.type(value)

##########################
# 读取配置文件
##########################
import configparser

config = configparser.ConfigParser()
config.read('config_parser.ini')
print(config['baseconf']['host'])
host = config['baseconf']['host']
print('host:'+ host)
print(isinstance(host,dict))
print(type(host))






