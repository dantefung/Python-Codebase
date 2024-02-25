from rediscluster import RedisCluster

redis_host = "127.0.0.1"

# Redis 集群节点
startup_nodes = [
    {"host": redis_host, "port": "7000"},
    {"host": redis_host, "port": "7001"},
    {"host": redis_host, "port": "7002"},
    {"host": redis_host, "port": "7003"},
    {"host": redis_host, "port": "7004"},
    {"host": redis_host, "port": "7005"},
    # 添加其他节点...
]

# 创建 Redis 集群连接
redis_client = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# 创建数据
def create_data(key, value):
    redis_client.set(key, value)
    print(f"Data with key '{key}' and value '{value}' has been created.")

# 读取数据
def read_data(key):
    value = redis_client.get(key)
    if value is not None:
        print(f"Data with key '{key}' has value '{value}'.")
    else:
        print(f"Data with key '{key}' does not exist.")

# 更新数据
def update_data(key, new_value):
    if redis_client.exists(key):
        redis_client.set(key, new_value)
        print(f"Data with key '{key}' has been updated to '{new_value}'.")
    else:
        print(f"Data with key '{key}' does not exist.")

# 删除数据
def delete_data(key):
    if redis_client.exists(key):
        redis_client.delete(key)
        print(f"Data with key '{key}' has been deleted.")
    else:
        print(f"Data with key '{key}' does not exist.")

if __name__ == "__main__":
    # 演示 CRUD 操作
    key = "name"
    value = "John Doe"

    create_data(key, value)
    read_data(key)

    new_value = "Jane Smith"
    update_data(key, new_value)
    read_data(key)

    delete_data(key)
    read_data(key)