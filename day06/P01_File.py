"""
 该案例演示了文件的读写
"""
"""
# 文件的写入
# 打开文件
f = open("test.txt","w")

# 写入操作
f.write("hello python1 \n")
f.write("nihao python2 \n")

# 关闭文件
f.close()
"""
# 文件的读取
# 打开文件
f = open("test.txt","rt")

# 读取文件 -- read()
# read(不加参数)   读取文件所有内容
# print(f.read())
# read(加参数)     从文件中读取指定的字节数
# print(f.read(5))
# print(f.read(8))
# readline(不加参数)   从文件中按行读取数据
# readline(加参数)   从文件中读取指定的字节数
# print(f.readline())
# print(f.readline(5))

# 从文件中读取多行数据，放到list中
# readlines([size]) 读取所有行并返回列表，若给定 size>0，返回总和大约为 size 字节的行， 实际读取值可能比 size 大
print(f.readlines())

# 关闭文件
f.close()

# 递归的遍历目录的内容
import os
print(os.getcwd())
for root, dirs, files in os.walk("E:\code_space\python20260824"):
    print("当前路径：",root)
    print("目录：",dirs)
    print("文件：",files)
    print()