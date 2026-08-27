"""
    晨测题
"""
"""
# 编写一个 Python 程序，获取用户输入的整数，判断它是正数、负数还是零，并输出相应的结果
num = input("请输入一个整数：")
num_int = int(num)
if num_int > 0:
    print("正数")
elif num_int < 0:
    print("负数")
elif num_int == 0:
    print("0")
"""
"""
# 模拟用户登录验证，获取键盘上的输入，如果用户名root,密码是123456，提示登录成功，否则提示登录失败
user_name = input("用户名：")
password = input("密码：")
if user_name == "root" and password == "123456":
    print("登录成功")
else:
    print("登录失败")
"""
"""
# 从键盘上输入3位正整数，判断是否为水仙花数
# 水仙花数:3位正整数等于各位数字的立方和
str_num = input("请输入3位正整数：")
int_num = int(str_num)

g = int_num % 10
s = int_num // 10 % 10
b = int_num // 100

if int_num == g**3 + s**3 + b**3:
    print(f"{int_num}是水仙花数")
else:
    print(f"{int_num}不是水仙花数")
"""