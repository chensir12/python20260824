"""
    该案例演示了带包模块的导入
"""
import time
"""
# 全局导入
import graphic.circle
print(graphic.circle.PI)

import graphic.circle as c
print(c.PI)
"""
# 使用 import 时，除最后一项外都必须是包。最后一项可以是模块或包，但不能是类、函数或变量。
import graphic

# print(graphic.circle.PI)
# 局部导入包下的模块 from import
from graphic import rectangle
print(rectangle.rectangle_width)

# 局部导入包下模块的成员
from graphic.circle import area
print(area(10))

# 局部导入 from import * 从包中导入模块
from graphic import *
print(circle.PI)

import graphic.circle as c
print(c.PI)

# 打包自己的库并安装 后续要学习-------------
