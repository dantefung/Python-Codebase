from confluent_kafka import Consumer
import requests
import json

# pip install confluent-kafka
# pip install requests


def send_msg_to_weixin(msg):
    key = "你的key"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
    data = {
        "markdown": {
            "content": msg
        },
        "msgtype": "markdown"
    }
    ret = requests.post(url, json=data)
    print(f"ret: {ret}")


def keywordMatchAlarm(kafka_servers, group_id, topic, keywords):
    conf = {'bootstrap.servers': kafka_servers, 'group.id': group_id, 'auto.offset.reset': 'earliest'}
    c = Consumer(conf)
    c.subscribe([topic])
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        message = msg.value().decode('utf-8')

        print('Received message: {}'.format(message))

        msgPayload = json.loads(message) # 解析JSON格式的消息


        # for keyword in keywords:
        #     if keyword in message:
        #         send_msg_to_weixin(message)
        #         break
    c.close()

if __name__ == '__main__':

    send_msg_to_weixin("test")

    # keywords = ['keyword1', 'keyword2', ...] # 你的关键字列表
    # group_id = "you_group_id" # 你的消费者组id
    # topic = "your_topic" # 你的kafka主题
    # kafka_servers = "your_kafka_servers"
    # keywordMatchAlarm(kafka_servers, group_id, topic, keywords)



  

