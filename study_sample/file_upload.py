import requests
import datetime



def concurrentRequest():
    counter = 0
    total = 1
    #total  = 2000
    while counter < total:
        print('当前',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),' -- ','发起第',counter,'次请求...')
        counter += 1
        fileUpload()

def fileUpload():
    url = 'http://localhost:6020/app/schedule/employeescheduleresult/importExcelSchedules'
    fileName = 'E:/test/EHR_employee_schedule_model_只有一天.xlsx'
    # 要上传的文件
    files = {'file': open(fileName,'rb')}
    headers = {'Authorization': 'Basic PASSTHR', 'X-OS-KERNEL-TOKEN':'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwdGVzdCIsInVzZXJfbmFtZSI6InB0ZXN0IiwiX3VzZXJfbmFtZSI6ImhpbnMiLCJleHAiOjE2MDk2NDIxMzQsInVzZXJJZCI6IjBlMDhlMTUzYjA0YTExZTliMzFiYjA2ZWJmMTRhNDc2In0.IVp5zUQWqe0j5UNhO-HxEga2PVW2Za4XXrFxGKSSmtU'}

    r = requests.post(url, files=files, headers=headers)
    print(r.text)



# post携带的数据
#data = {'a': '杨', 'b': 'hello'}
#r = requests.post(url, files=files, data=data)
#r = requests.post(url, files=files, headers=headers)
#print(r.text)
concurrentRequest()