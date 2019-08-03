import socket

client = socket.socket()
ip_port = ('127.0.0.1', 8889)
# connect server
client.connect(ip_port)


while True:
    data = client.recv(1024)
    # print the data received
    # data need to be decode in python3.x
    print(data.decode())
    # 输入发送的消息
    msg_input = input('请输入发送的消息: ')
    client.send(msg_input.encode())
    if msg_input == 'exit':
        break
    data = client.recv(1024)
    print(data.decode())
