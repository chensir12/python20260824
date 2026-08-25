"""
    该案例演示了字符的编码和解码
    要求：编码的时候使用的字符集和解码的时候使用的字符集要一致
"""
# 编码：将字符转换为字节的过程
str1 = "你好中国"
byte1 = str1.encode(encoding="gbk")
print(byte1)
# 解码：将字节转换为字符的过程
str2 = byte1.decode(encoding="gbk")
print(str2)