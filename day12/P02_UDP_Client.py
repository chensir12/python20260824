"""
    UDP客户端
"""
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 循环
while True:
    server_addr = ('127.0.0.1',8888)
    msg = input("客户端说：")
    #向服务器发送消息
    udp_socket.sendto(msg.encode(), server_addr)
    #接收服务器返回的消息
    data, s_addr = udp_socket.recvfrom(1024)
    #将消息打印输出到控制台
    print(f"服务器说:{data.decode()}")

# 关闭套接字
udp_socket.close()
