import requests
import time

####### GLOBAL VARIABLE DEFINE START ###########

url = "http://jobctr-dev.xxx.cn/jobctr/jobinfo/trigger"
# user identity
cookie = "XXL_JOB_LOGIN_IDENTITY=7b226964223a312c22757365726e616d65223a2261646d696e222c2270617373776f7264223a223031393230323361376262643733323530353136663036396466313862353030222c22726f6c65223a312c227065726d697373696f6e223a6e756c6c7d"
arr = ['c77a36317c09731b1475bda91e1a6fd3', 'c77a36317c09731b1475bda91e1a6fd3', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# 休眠时间 单位:s
sleep = 1

####### GLOBAL VARIABLE DEFINE END ###########


# request the job trigger
def reqJobTrigger(url, data, cookie):
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie
    }
    res = requests.post(url=url, data=data, headers=header)
    print(res.text)


def prepareData(startIndex, endIndex):
    cmdPrefix = "5@0@0@2_"

    newArr = []
    for item in arr[startIndex:endIndex]:
        newArr.append(item + ':2')
    executorParam = cmdPrefix + ','.join(newArr)
    data = {
        "executorParam": executorParam,
        "id": "24"
    }
    return data


totalCount=arr.__len__()
pageSize = 4
pageNo = 1
if totalCount%pageSize == 0:
    totalPage = totalCount/pageSize
elif totalCount%pageSize > 0:
    totalPage = totalCount/pageSize + 1

while pageNo <= totalPage:
    startIndex = (pageNo-1) * pageSize
    endIndex = startIndex + pageSize
    data = prepareData(startIndex, endIndex)
    print(data)
    print("当前时间: %s" % time.ctime())
    # 调用sleep()函数让当前线程暂停1s
    time.sleep(sleep)
    reqJobTrigger(url, data, cookie)
    pageNo = pageNo + 1

# arr = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
# pageSize = 4
# pageNo = 4
# startIndex = (pageNo-1) * pageSize
# endIndex = startIndex + pageSize
# print(arr[startIndex:endIndex])
# print(','.join(arr[startIndex:endIndex]))
# for i in arr[startIndex:endIndex]:
#     print(i)
