#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import math
import time

PY_MYSQL_CONN_DICT = {
    "host" : 'x.x.x.x',
    "port" : 3306,
    "user" : 'dev',
    "passwd" : 'dev@123',
    "db" : 'erp_ods'
}


mysql = pymysql.connect(**PY_MYSQL_CONN_DICT)
mysql_cursor = mysql.cursor(cursor=pymysql.cursors.DictCursor)
mysql_cursor.execute("SELECT count(1) from dcp_dwm_erp_sku_stat_month where merchant_id = 'b7337c0a-7a97-4c1f-934c-6c1926594990'")
totalCount = mysql_cursor.fetchone()[0]
pageSize = 50
pageNo = 2
# startIdx = (pageNo -1)*pageSize
offset = pageSize
totalPage = (totalCount/pageSize) if totalCount%pageSize == 0 else math.floor((totalCount/pageSize)) + 1
startTime = time.clock()
print("开始执行时间:{0}".format(startTime))
try:
    while pageNo <= totalPage:
        startIdx = (pageNo -1)*pageSize
        print(">>>>>>>totalCount:{0}  totalPage:{1}  pageSize:{2}  pageNo:{3}   startIdx:{4}  offset:{5}".format(totalCount, totalPage, pageSize, pageNo, startIdx, offset))
        mysql_cursor.execute("select t.id from dcp_dwm_erp_sku_stat_month t where t.merchant_id = 'b7337c0a-7a97-4c1f-934c-6c1926594990' order by t.id asc limit {0},{1}".format(startIdx, pageSize))
        ret = mysql_cursor.fetchall()
        startId = ret[0][0]
        endId = ret[len(ret)-1][0]
        print(">>>>>>>处理从startId:{0} 到 endId:{1} 的数据 ... ".format(startId, endId))

        mysql_cursor.callproc( "sku_stat_by_month_updating", args=(startId,endId))
       #mysql_cursor.execute("update dcp_dwm_erp_sku_stat_month set gross_sale = '0' where id = '2'")
        results=mysql_cursor.fetchone()
        print(results)
        print(results[0])
        pageNo = pageNo + 1
    # for i in range(180000,189999,50):
    #     print("处理从%d到%d的数据" %(i,i+49))
    #     mysql_cursor.execute( "call sku_stat_by_month_updating({0}, {1});".format(i,i+49) )
    #     results=mysql_cursor.fetchone()
    #     print(results[0])
        endTime = time.clock()
        print("finish! endTime:{0} 耗时:{1}", endTime, (endTime-startTime))
except Exception as e:
    mysql.rollback()
    raise e
finally:
    mysql_cursor.close()
    mysql.close()
