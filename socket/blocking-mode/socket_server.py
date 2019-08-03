import socket
import random

sk = socket.socket()
ip_port = ('127.0.0.1', 8889)
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
# 不断循环,不断接收数据
while True:
    # 提示信息
    print("正在进行等待接受数据......")
    # 接收数据
    conn, address = sk.accept()
    # 定义信息
    msg = "Hello World!"
    # 返回信息
    # python3.x以上,网络数据的发送接收都是byte类型的
    # 如果发送的数据是str类型的,则需要进行编码
    conn.send(msg.encode())
    # 不断接收客户端发来的消息
    while True:
        # 接收客户端消息
        data = conn.recv(1024)
        print(data.decode())
        # 接收到退出命令
        if data == b'exit' or data == b'quit':
            break
        # 处理客户端数据
        conn.send(data)
        conn.send(str(random.randint(1, 100)).encode())
    # 主动关闭连接
    conn.close()

