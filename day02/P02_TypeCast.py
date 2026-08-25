"""
    该案例演示了类型转换
"""
"""
# 相同数据类型的变量进行计算，没有涉及类型转换
num1 = 10
num2 = 20
num3 = num1 + num2
print(type(num1))
print(num3)
print(type(num3))
"""
"""
# 隐式转换（自动类型转换）：对两种不同类型的数据进行运算，较小的类型就会转换成较大的类型以避免数据丢失
num1 = 10
f1 = 5.0
res = num1 + f1
print(type(num1))
print(type(f1))
print(res)
print(type(res))
"""
"""
# 两个整型进行除法运算结果也是浮点型
num1 = 10
num2 = 2
num3 = num1 / num2
print(type(num1))
print(type(num2))
print(num3)
print(type(num3))
num4 = num1 // num2
print(type(num4))
"""
"""
# 整型和字符串相加会报错
num1 = 10
str1 = "20"
print(num1 + str1)
"""
"""
# int(x [,base]) 将x转换为一个十进制整数，x若为字符串可用base指定进制
res = int('110',2)
print(res)
res = int('110',8)
print(res)
res = int('110',16)
print(res)
# float(x) 将x转换为一个浮点数
print(float('1.0'))
"""

# complex(real [,imag]) 创建一个实部为real，虚部为imag的复数
print(complex(3,2))
# str(x) 将对象x转换为一个字符串
print(str("hello \n world"))
# repr(x) 将对象x转换为一个字符串，可以转义字符串中的特殊字符
print(repr("hello \n world"))

# eval(x) 执行x字符串表达式，并返回表达式的值
eval("print(123)")
# bin(x) 将一个整数转换为一个二进制字符串
print(bin(10))
# cot(x) 将一个整数转换为一个八进制字符串
print(oct(10))
# hex(x) 将一个整数转换为一个十六进制字符串
print(hex(10))

# ord(x) 将一个字符转换为它的ASCII整数值
print(ord('a'))

# chr(x) 将一个整数转换为一个Unicode字符
print(chr(98))

