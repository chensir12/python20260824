"""
    TCP服务端
"""
import socket
import threading
from random import randint

"""
# 版本1
# 创建套接字对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
tcp_socket.bind(('127.0.0.1', 8888))
# 设置监听
tcp_socket.listen(70)
# 等待客户端连接
c_socket,c_addr = tcp_socket.accept()
# 循环
while True:
    # 接收客户端发送的消息
    data = c_socket.recv(1024)
    if not data:
        break
    # 将客户端消息打印输出到控制台
    print(f"客户端{c_addr[0]}说:{data.decode()}")
    # 向客户端发送消息

# 关闭套接字对象
c_socket.close()
tcp_socket.close()
"""
"""
# 版本2   服务器端输入消息
# 导包
import socket

# 创建套接字对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
tcp_socket.bind(('127.0.0.1', 8888))
# 设置监听
tcp_socket.listen(70)
# 等待客户端连接
c_socket,c_addr = tcp_socket.accept()
# 循环
while True:
    # 接收客户端发送的消息
    data = c_socket.recv(1024)
    if not data:
        break
    # 将客户端消息打印输出到控制台
    print(f"客户端{c_addr[0]}说:{data.decode()}")
    # 向客户端发送消息
    msg = input("服务器说:")
    if not msg:
        msg = "None"
    c_socket.send(msg.encode())

# 关闭套接字对象
c_socket.close()
tcp_socket.close()
"""
"""
# 版本3      服务器向客户端发送随机消息
# 导包
import socket

# 创建套接字对象
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
tcp_socket.bind(('127.0.0.1', 8888))
# 设置监听
tcp_socket.listen(70)
# 等待客户端连接
c_socket,c_addr = tcp_socket.accept()
# 循环
while True:
    # 接收客户端发送的消息
    data = c_socket.recv(1024)
    if not data:
        break
    # 将客户端消息打印输出到控制台
    print(f"客户端{c_addr[0]}说:{data.decode()}")
    # 向客户端发送消息
    msg_list = ["您好","在呢","您想咨询什么？","要大模型资料吗？","加V哦","我可以给你发送课程资料"]
    c_socket.send(msg_list[randint(0,len(msg_list)-1)].encode())

# 关闭套接字对象
c_socket.close()
tcp_socket.close()
"""
# 版本4    可以连接多个客户端 并针对每一个客户端开启新的线程进行处理   +  异常
import socket

# 针对每一个客户端进行处理的函数
def handle_client(c_socket, c_addr):
    try:
        # 循环
        while True:
            # 接收客户端发送的消息
            data = c_socket.recv(1024)
            if not data:
                break
            # 将客户端消息打印输出到控制台
            print(f"客户端{c_addr[0]}说:{data.decode()}")
            # 向客户端发送消息
            msg_list = ["您好", "在呢", "您想咨询什么？", "要大模型资料吗？", "加V哦", "我可以给你发送课程资料"]
            c_socket.send(msg_list[randint(0, len(msg_list) - 1)].encode())
    except:
        print(f"和客户端{c_addr[0]}通信发生了异常")
    finally:
        c_socket.close()

if __name__ == '__main__':
    # 创建套接字对象
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP和端口
    tcp_socket.bind(('127.0.0.1', 8888))
    # 设置监听
    tcp_socket.listen(70)

    while True:
        # 等待客户端连接
        c_socket, c_addr = tcp_socket.accept()
        # 针对每一个客户端开启一个新的线程进行处理
        t = threading.Thread(target=handle_client, args=(c_socket, c_addr))
        t.start()

    tcp_socket.close()