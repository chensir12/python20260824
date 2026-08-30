"""
    提供一个函数，实现文件的拷贝
"""
"""
# 基础版
# source_file_path 源文件路径
# dest_file_path 目标文件路径
def copy_file(source_file_path,dest_file_path):
    source_file = open(source_file_path, "rb")
    # 打开目标文件夹
    dest_file = open(dest_file_path, "wb")
    content = source_file.read()
    dest_file.write(content)

    # 关闭
    source_file.close()
    dest_file.close()

copy_file(r"F:\test.jpg","F:\\copy.jpg")
"""

# 优化1： 读取指定的字节  然后将读取的字节写到目标文件
def copy_file(source_file_path,dest_file_path):
    source_file = open(source_file_path, "rb")
    dest_file = open(dest_file_path, "wb")

    content = source_file.read(1024)
    while content:
        # 将读取的数据写到目标文件
        dest_file.write(content)
        # 继续读取文件
        content = source_file.read(1024)
    # 关闭
    source_file.close()
    dest_file.close()

copy_file(r"F:\187 4K.mp4","F:\\copy.mp4")

# 优化2： 海象运算符 ，在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增
def copy_file(source_file_path,dest_file_path):
    # 从源读取数据
    # 打开源文件
    source_file = open(source_file_path,"rb")
    # 打开目标文件
    dest_file = open(dest_file_path,"wb")

    # 从源文件中读取指定字节数据
    while content := source_file.read(1024):
        # 将读取的数据写到目标文件
        dest_file.write(content)


    # 关闭
    source_file.close()
    dest_file.close()