import time
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import base64
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
import requests
import urllib
import json

'''
依赖包:
pip install requests
pip install crypto pycryptodome
pip uninstall crypto pycryptodome
pip install pycryptodome
'''

## 开启代理让fiddler可以抓包
proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy)

# 接入方私钥
privateKey = 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCDpMiE1vS8EGXnj8aMOAd7QT+7BWZMI9Io8IBQe3F7x7vlc/VoT0puMPf8+Hi5F+MLWTByDGjDGi/zJTQDmsfdrlcrBSbTOkyvg4jNOuiT15vFXYXklgm9nlLHm3NBAxP3tnWjdMsSCjAAgMy4mIjBVcafhbxVmXXV54D1HLadC0zThyPu0eUqkdqnlS+XdbskODp7iNLVN70KWse0Xn2wdO/pjV/tsoAye2FraTlR0Wtsa/BIo/f+z/gPikJr0q4eohoVGgPA2pAMIQ0Wg0aQMBkkxXOwbpx4ZwLicVHTNTWUWKITQlw5SCODbmW7Zu1x+CT8ihSyUc+UB4Szb487AgMBAAECggEAKubS6mfbTkbRzwtOG3hPB94V1O9HjVzHKsxmJNR2AW7wTzDhM2NT0GFpECoxvbCJL7ObVC+zHJI2OjlPoDUbGaWthrmhE4mWYESvmqKuFTBY9ZMrBXnYJtGoDKEeiHtmUH5IDEMNww1K438WOLqNJuS7XFWLMSJYAqP1pOv8n2ULyoGLBVdvtXKQD9haUnLq8LBGadfgXyzMQ9byL29F6CG029F5H54aA37ImswQ67XUo5B9WNWE/3cN1okzVKMbRln6ZM/t74Ga2oIVhkKIK2bP0lAzdczjTFHdPt60kkU4bna3JX59ii15bx1JDWqZTmAsJTZycp9qk4+zjnsN8QKBgQDbk2wUcdDrJwpoV78xrRwF+5pcIKpYgkHM/dUhaBU0+v8D2bAj9k8yXDGtEKsLmOEPTkcYWqxl0paRJ7hWAsgJkiw0m/DWNyS5J0N2zd2UdAepP9r4JD+TFsWfodDqFnnd96fEAoB4ctI0ngn9tveVfVuqLJx7WAm/YYMFtE+aDQKBgQCZezSSmyfMk2Is7mI0J7Rgzg8Nb2LHPQ9a4r9yTCxC8EsSYBhvOuERKwU26ZwRxf6qxy7UONJ2wri6JGjUobsUbw41E2UHF9j0WsYkSpy/uh+f5a7LWe8Eef8NeIfQ/OJWM5UpABO3/mx+JbmmVjuH423rWHFzXiSFoDYeBsnkZwKBgQCXk3BDuMIo4p17pD83ErJKqwJG4MHXMawsz3kmg4xIM5CBXvAKE0lekWg1eVEqQ1Hx1+6aMFXcQIByGcJVlbvzZ3Wep5uctRpjumgHBlwU0/hJ7OvC6nr8lfa8mN74CaX9Ba5JUBTRkSns6sAo5fqJtqzlj8BCIWcxNyZUdMGSrQKBgDvJ7Q73dieRens6WfMrTG8xlleLfpVSyfqDvkSOO+fPp87+tEYQT8DaW2uq0WtzD+QDN9DgWcx9ymxo5pV+c1xgbs5qQb7joVZ/ThSxJCLkJJGrbc41uJCr3ZmnzHCzMpCWA5M3Pnc8m5MAqzOLACHNjPJTP87La7rKUIqd5mQdAoGAeD4FZe4ByqZs76Q1D/ouRoywXhrpa+/+wpJaIpNHfUaRCKc3ISSe228DnkwnYl2KosQC+W3r04wKwxcWdnGIFsz3RDKA18wIivRqZErqpNFpi1TeFw72+TUe/0m2E0ekU45hwl0yWphM74at4Pjt/kLtUoisp2/R5km22dTDnE0='
# 接入方公钥
publicKey = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAg6TIhNb0vBBl54/GjDgHe0E/uwVmTCPSKPCAUHtxe8e75XP1aE9KbjD3/Ph4uRfjC1kwcgxowxov8yU0A5rH3a5XKwUm0zpMr4OIzTrok9ebxV2F5JYJvZ5Sx5tzQQMT97Z1o3TLEgowAIDMuJiIwVXGn4W8VZl11eeA9Ry2nQtM04cj7tHlKpHap5Uvl3W7JDg6e4jS1Te9ClrHtF59sHTv6Y1f7bKAMntha2k5UdFrbGvwSKP3/s/4D4pCa9KuHqIaFRoDwNqQDCENFoNGkDAZJMVzsG6ceGcC4nFR0zU1lFiiE0JcOUgjg25lu2btcfgk/IoUslHPlAeEs2+POwIDAQAB'
# 我方私钥
selfPrivateKey = 'TODO:自己生成'
# 我方公钥
selfPublicKey = 'TODO:自己生成'
# 分配给第三个方的appId
appSysId = 'fhltest2d887f6e6d54478c82c7c3701'


def genPrivateKeyByPKStr():
    length = privateKey.__len__()
    print('private Key length:', length)
    group = length / 64
    print('before adjust:', group)
    group = group if (length % 64) == 0 else (int(group) + 1)
    print('after adjust:', group)

    finalStr = '-----BEGIN RSA PRIVATE KEY-----\n'
    step = 1
    while step <= group:
        sIdx = (step - 1) * 64
        eIdx = sIdx + 64
        # print('step', step,' sIdx: ', sIdx, '-- eIdx:', eIdx ,':', privateKey[sIdx:eIdx])
        finalStr = finalStr + privateKey[sIdx:eIdx] + '\n'
        step = step + 1
    finalStr = finalStr + '-----END RSA PRIVATE KEY-----'
    print(finalStr)
    with open('private.pem', 'w+') as f:
        f.write(finalStr)


def genPublicKeyByPKStr():
    length = publicKey.__len__()
    print('public Key length:', length)
    group = length / 64
    print('before adjust:', group)
    group = group if (length % 64) == 0 else (int(group) + 1)
    print('after adjust:', group)

    finalStr = '-----BEGIN RSA PUBLIC KEY-----\n'
    step = 1
    while step <= group:
        sIdx = (step - 1) * 64
        eIdx = sIdx + 64
        # print('step', step,' sIdx: ', sIdx, '-- eIdx:', eIdx ,':', privateKey[sIdx:eIdx])
        finalStr = finalStr + publicKey[sIdx:eIdx] + '\n'
        step = step + 1
    finalStr = finalStr + '-----END RSA PUBLIC KEY-----'
    print(finalStr)
    with open('public.pem', 'w+') as f:
        f.write(finalStr)


def signByPrivKey(message):
    print('使用私钥:', privkey, '加密')
    signer = PKCS1_signature.new(privkey)
    digest = SHA256.new()
    digest.update(message.encode("utf8"))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    print(signature.decode('utf-8'))
    return signature.decode('utf-8')


def getToken():
    # 认证中心获取token请求地址
    authUrl = "xxxxx"
    # 当前系统时间戳
    timestamp = str(int(time.time()))
    print('timestamp:', timestamp)
    # 明文=appSysId + timestamp
    plainText = appSysId + timestamp
    print('plainText:', plainText)
    # 私钥签名
    signature = signByPrivKey(plainText)
    print('signature:', signature)

    headers = {'Content-Type': 'application/json', 'X-OS-BOOT-APPSYSID': appSysId}
    payload = {'appSysId': appSysId, 'timestamp': timestamp, 'signValue': signature}
    print('request body:', json.dumps(payload))
    ## 用下面的方法请求会变成这种格式  appSysId=fhltest2d887f6e6d54478c82c7c3701&timestamp=1590133637&signValue=BGWatU9A7GV2lulTx2Cp5FdQei7xrG%2FwtjKDhPFmoEZcJyrNEQT5nUfvTpBAP6yIks%2FT2eaTBc4Mj0ECxxkwXJoM8CXsZBBQxM4DrC%2Fdkr0eRUqeqoid%2BGuVyv2HnoUbpXBkbMHnSAT7aW0nRqBlGEuKXzPHG6o9MjVXhWuSFGZvdNLSSI8wATOcoZUKq%2B6g1BG20xivDChCJrIYfEMAEbaCoJulH7T9vRHKknrRgryW%2Beaxb7I5tkdTIUffg9nSrxcICJ1jaGg9v093ZGPWLXHNl1%2B%2F%2F5hOCwsT%2BBpFLSfxM1znfhps1PxMLt9w92ZJF%2FM3ykWx3FFK%2B9qB45VY%2Fw%3D%3D
    ## 会导致JSON解析出错
    # r = requests.post(authUrl, headers=headers, data=payload)
    r = requests.post(authUrl, headers=headers,data=json.dumps(payload))
    print('status_code:', r.status_code)
    print('response content:', r.content.decode('utf-8'))
    token = ''
    # 将 JSON 对象转换为 Python 字典
    resDict = json.loads(r.content.decode('utf-8'))
    if resDict['code'] == 0:
        token = resDict['result']['token']
    print('申请到的token:', token)
    return token

def testRequestSaveOrder():
    bizUrl = "yyyyyy"
    token = getToken()
    print('-------------->token:', token)
    # 当前系统时间戳
    timestamp = str(int(time.time()))
    # 品牌名称
    brandName = '测试2'
    # 公司名称
    companyName = '58姐'
    # 订单备注
    remarks = ''
    # 联系人
    contacts = '老麦'
    # 联系电话
    contactPhone = '130123123123'
    # 点位资产编码
    advertNo = '4401-GTLS-ZQ-ZS-STLN18-015-C'
    # 保证金
    guaranteeAmount = '0'
    # 广告总报价
    publicPrice = '1000'
    # 订单金额
    orderAmount = '1200'
    # 广告投放开始时间 2021-01-21
    startDay = '2021-01-21'
    # 广告投放结束时间
    endDay = '2021-02-25'
    # 上刊素材可访问url
    materialUrl = 'http://www.baidu.com'
    # 上刊素材开始投放时间
    materiaStartDay = '2021-01-21'
    # 上刊素材结束投放时间
    materialEndDay = '2021-02-25'

    payload = {
                'brandName':brandName,
                'companyName':companyName,
                'remarks':remarks,
                'contacts':contacts,
                'contactPhone':contactPhone,
                'advertNo':advertNo,
                'guaranteeAmount':guaranteeAmount,
                'publicPrice':publicPrice,
                'orderAmount':orderAmount,
                'startDay':startDay,
                'endDay':endDay,
                'materialEntityList':[{
                        'materialUrl':materialUrl,
                        'startDay':materiaStartDay,
                        'endDay':materialEndDay
                    }
                ]
    }

    print('request body:', json.dumps(payload))
    wait4SignText = json.dumps(payload) + appSysId + token + timestamp
    print('拼接后的字符串:', wait4SignText)
    sign = signByPrivKey(wait4SignText)

    headers = {
                'Content-Type': 'application/json',
                'Authorization':'Basic PASSTHR',
                'X-OS-BOOT-APPSYSID': appSysId,
                'X-OS-BOOT-TOKEN': token,
                'X-OS-BOOT-TIMESTAMP':timestamp,
                'X-OS-BOOT-SIGN':sign
    }
    r = requests.post(bizUrl, headers=headers, data=json.dumps(payload))
    print(r.content.decode('utf-8'))


# 生成私钥文件
genPrivateKeyByPKStr()
# 生成公钥文件
genPublicKeyByPKStr()

# -----------------导入密钥 START----------------
with open('public.pem', 'r') as f:
    publicKeyFmt = f.read()

with open('private.pem', 'r') as f:
    privateKeyFmt = f.read()

print(publicKeyFmt)
pubkey = RSA.importKey(str(publicKeyFmt))
privkey = RSA.importKey(str(privateKeyFmt))
print('pubkey:', pubkey)
print('privkey:', privkey)
# -----------------导入密钥 END----------------

# 申请token
#getToken()
# 下单接口
testRequestSaveOrder()


