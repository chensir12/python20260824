"""
    TCP客户端
"""
import socket

# 创建套接字对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
server_addr = ("127.0.0.1",8888)
tcp_socket.connect(server_addr)
# 循环
while True:
    msg = input("客户端说:")
    if not msg:
        msg = "None"
    # 向服务器发送消息
    tcp_socket.send(msg.encode())
    # 接收服务器返回的消息
    data = tcp_socket.recv(1024)
    # 将服务器返回的消息打印到控制台
    print(f"服务器说:{data.decode()}")

# 关闭套接字对象
tcp_socket.close()
