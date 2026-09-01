"""
    该案例演示了模块的导入
"""
"""
# 全局导入
import P02_My_Add
print(P02_My_Add.num)
print(P02_My_Add.num1)
print(P02_My_Add.add(10, 20))

import P02_My_Add as ma
print(ma.num)
print(ma.add(10, 20))
"""
"""
# 局部导入方式1 from import
# 指定导入模块的部分成员，直接通过成员名的方式访问。
# 只能使用其导入的成员,未导入的成员不能使用。如果多个模块中存在重名成员，后一次导入会覆盖前一次导入。
from P04_My_Multi import multi
# print(num)
print(multi(3, 4))

# 重名变量 后一次导入会覆盖前一次导入
from P02_My_Add import num
from P04_My_Multi import num
print(num)

# 通过别名区分不同模块的变量
from P02_My_Add import num as n1
from P04_My_Multi import num as n2
print(n1)
print(n2)

# 局部导入 方式2 from 模块名 import *
# 导入模块中所有不以单下划线开头的成员，直接通过成员名的方式访问
import P04_My_Multi as mm
print(mm._str1)
"""
"""
from P04_My_Multi import *
print(num)
print(multi(3, 4))
# print(_str1)
"""
"""
# 模块搜索顺序
import sys

print(sys.path)
sys.path.append("./..")
print(sys.path)
"""
# __all__ 限制被导入的成员
from P02_My_Add import *
print(num)
# print(num1)
# print(_str1)
print(add(10, 20))

# dir()
#当你将一个模块作为 dir() 的参数时，它会返回该模块中定义的名称列表，包括函数、类、变量等 dir(模块名)
import math
print(dir(math))

# 当你将一个对象作为dir()的参数时，它会返回该对象的属性和方法列表
class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2

    def method1(self):
        pass
obj = MyClass()
print(dir(obj))

# 当你不传递任何参数调用dir()时，它会列出当前作用域中定义的名称，包括变脸，函数，类等
def m1(aa,bb):
    print(dir())
m1(1,2)

print(dir())


