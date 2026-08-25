"""
    该案例演示了运算符
"""

from traceback import print_tb

from numpy.testing.print_coercion_tables import print_new_cast_table

"""
# 算术运算符
print(10 + 5)
print(10 - 5)
print(-5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
"""
"""
# 赋值运算符
a = 10
a = a + 1
a += 1
print(a)

num1 = 10
num2 = 20
print((num3 := num1 + num2) > num1)
print(num3)
"""
"""
# 比较运算符
num1 = 10
num2 = 20
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# 不同类型的数据之间不能进行比较
str3 = "15"
# print(num2<str3)
str5 = "6"
print(str3>str5)
"""
"""
# 逻辑运算符
# 与，x and y，若x为False返回x的值，否则返回y的值
b1 = False
b2 = True
print(b1 and b2)
print(b2 and b1)

# 或，x or y，若x为True返回x的值，否则返回y的值
x = 0
y = 8
print(x or y)

print(not x)
"""
# 成员运算符
list1 = [10,20,30]
print(100 not in list1)
print(10 in list1)

# 身份运算符
num1 = 10
num2 = 1
print(num1 == num2)
print(num1 is num2)
b1 = True
print(num2 == b1)
print(num1 is b1)

#import sys;for i in sys.path:;print(i) #报错

import sys
for item in sys.path:print(item) # 没有问题

for i in sys.path:
    print(i) # 没有问题




