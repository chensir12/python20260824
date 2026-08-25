"""
    该案例演示了数据类型
"""

"""
# 整数类型
int1 = 10
num1 = 1_000_000_000_000
print(type(int1))
print(num1)

# 定义一个bool类型
num1 = True

# 定义一个整数类型变量
num2 = 20
print(type(num1))
print(type(num2))

print(type(num1) == type(num2))
print("~~~~~~~")
print(isinstance(num1, bool))
print(isinstance(num2, int))

print(isinstance(num1, int)) #python3中 bool是int的子类
"""

"""
# 小整数池 [-5, 256]
num1 = 10
num2 = 10
num3 = 10
# id() 查看变量的内存地址
print(id(num1))
print(id(num2))
print(id(num3))
num4 = 300
num5 = 300
print(id(num4))
print(id(num5))
"""

"""
# 浮点数类型
f1 = 0.1
f2 = 0.2
print(type(f1))
print(type(f2))
f3 = f1 + f2
print(f3) # float有微小的误差

# 从decimal模块中导入Decimal类
from decimal import Decimal
# 创建decimal类型对象
f4 = Decimal('0.1')
f5 = Decimal('0.2')
print(type(f4))
f6 = f4 + f5
print(f6)

num1 = 1.3e7
print(num1)
"""

"""
# bool类型
b1 = True
b2 = False
print(type(b1))
print(type(b2))

print(b1 == 1)
print(b2 == 0)

# 判断b1和1是不是同一个对象(是不是执行内存中的同一个地址)
print(b1 is 1)
b3 = True
print(id(b1), id(b3))
print(b1 is b3)
"""

# 字符串类型
# 字符串类型可以用单引号括起来
str1 = 'hello world'
str2 = 'hello "world"'
print(str1,str2)
# 字符串可以使用双引号括起来
str1 = "hello world"
str2 = "hello 'world'"
print(str1,str2)
print(type(str1))

# 用三个引号原样输出字符串内容
str1 = """
    hello world!
        hello python!
    hello atguigu!
"""
print(str1)
# 以下语法报错
# str1 = ("hello"
#         world")
# 解决方案语法不报错，但是没有换行
str1 = ("hello "
        "world!")
# \ 在行尾作为续行符
print("hello \
      world")
print(str1)
# 解决方案--- 可以实现换行效果
str1 = "hello \n world"
print(str1)
str1 = "hello\rwor"
print(str1)

# 字符串的intern机制
str1 = "hello world"
str2 = "hello world"
print(id(str1))
print(id(str2))

str3 = "zs\tls\tww"
print(str3)

