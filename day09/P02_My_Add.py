__all__ = ["num","add"]
# 使用from import *导入模块时，可以在被导入的模块中使用 __all__设置哪些内容可以被导入。
# __all__ 的设置只针对使用 from import * 导入模块时有效
num = 100
num1 = 200
_str1 = "abc"

def add(a, b):
    """求两个数的和"""
    return a + b

print(__name__)

if __name__ == '__main__':
    print(add(10, 20))