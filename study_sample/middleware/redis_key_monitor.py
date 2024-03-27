from rediscluster import RedisCluster


class KeyDeleteListener:
    def __init__(self, cluster):
        self.configKeySpaceEvent(cluster)
        self.cluster = cluster
        self.pubsub = self.cluster.pubsub(ignore_subscribe_messages=True)

    def configKeySpaceEvent(self, cluster):
        # 配置notify-keyspace-events为EA
        response = cluster.config_set('notify-keyspace-events', 'EA')
        if response:
            print("Configuration set successfully")

    def start_listening(self, key_pattern, careAboutKeys, db=0):
        channel = f'__keyevent@{db}__:{key_pattern}'
        # channel = f'__keyspace@{db}__:{key_pattern}'
        self.pubsub.psubscribe(channel)
        print(f"Listening for key deletions on pattern '{key_pattern}'...")
        while True:
            message = self.pubsub.get_message()
            if message:
                # print(message)
                if message['type'] == 'pmessage':
                    # {'type': 'pmessage', 'pattern': '__keyevent@0__:del*', 'channel': '__keyevent@0__:del', 'data': 'platform_api-hk:ercp-api-statisticssearch'}
                    key = message['data']
                    # print(f"key: '{key}'")
                    self.printConcerned(careAboutKeys, key)

                    # event_type, _, key = message['data'].split()
                    # if event_type == 'del':
                    #     print(f"Key deletion detected: {key}")
                        # 在这里执行您希望对key删除事件进行的处理逻辑

    def printConcerned(self, careAboutKeys, key):
        # 匹配前缀是否符合
        if any(key.startswith(word) for word in careAboutKeys):
            print(f"{key} |    starts with one of the words in the list")
        elif key in careAboutKeys:
            # 匹配完全等于
            print(f"{key}  |   is in the list")

        else:
            # print(f"{key} is not in the list and does not start with any word in the list")
            pass

    def stop_listening(self):
        self.pubsub.close()
        self.cluster.connection_pool.disconnect()


if __name__ == '__main__':
    # 示例用法
    # Redis集群的所有节点
    startup_nodes = [
        {'host': '127.0.0.1', 'port': '7000'},
        {'host': '127.0.0.1', 'port': '7001'},
        {'host': '127.0.0.1', 'port': '7002'},
        {'host': '127.0.0.1', 'port': '7004'},
        {'host': '127.0.0.1', 'port': '7005'},


    ]
    keys = [
        "search:goods:"
    ]
    # 建立Redis集群连接
    rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    listener = KeyDeleteListener(cluster=rc)
    # listener.start_listening(key_pattern='your_key_pattern_*')  # 替换为要监听的key前缀或通配符
    listener.start_listening(key_pattern='del*', careAboutKeys=keys)  # 替换为要监听的key前缀或通配符
    # listener.printConcerned(['search:'], 'aaaaa')
