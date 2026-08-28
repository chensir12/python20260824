"""
    该案例演示了函数的定义
"""
"""
# 案例：在控制台打印输出一个2x3的*
rows = 2
while rows > 0:
    print("*" * 3)
    rows -= 1
print("-"*50)
rows = 2
while rows > 0:
    print("*" * 3)
    rows -= 1

# 抽取函数
def print_star():
    rows = 2
    while rows > 0:
        print("*" * 3)
        rows -= 1
print_star()
print("-"*50)
print_star()
"""
"""
# 不封装函数
rows = 2
while rows > 0:
    print("*" * 3)
    rows -= 1
print("-"*50)
rows = 3
while rows > 0:
    print("*" * 4)
    rows -= 1
"""
"""
# 封装函数 --- 没有参数
def print_star_1():
    rows = 2
    while rows > 0:
        print("*" * 3)
        rows -= 1

def print_star_2():
    rows = 3
    while rows > 0:
        print("*" * 4)
        rows -= 1
print_star_1()
print("-"*50)
print_star_2()
"""
"""
# 封装带参数的函数
# 定义通用的函数  打印rows 行 cols列 的*
def print_star(rows,cols):
    while rows > 0:
        print("*" * cols)
        rows -= 1

print_star(2,3)
print("-"*50)
print_star(3,4)
"""
"""
# 函数参数是不可变类型
def change_int(a):
    print(f"2在函数体中修改前值:{a},地址{id(a)}")
    a = 100
    print(f"3在函数体中修改后值:{a},地址{id(a)}")

b = 10
print(f"1在函数外调用函数前值:{b},地址{id(b)}")
change_int(b)
print(f"4在函数外调用函数后值:{b},地址{id(b)}")
"""
"""
# 函数参数是可变类型
def change_list(list1):
    print(f"2在函数体中修改前值:{list1},地址{id(list1)}")
    list1[2] = 666
    print(f"3在函数体中修改后值:{list1},地址{id(list1)}")

list3 = [10,20,30]
print(f"1在函数外调用函数前值:{list3},地址{id(list3)}")
change_list(list3)
print(f"4在函数外调用函数后值:{list3},地址{id(list3)}")
"""

def change_list(list1):
    print(f"2在函数体中修改前值:{list1},地址{id(list1)}")
    list1 = list1 * 2
    # list1 *=  2
    print(f"3在函数体中修改后值:{list1},地址{id(list1)}")

list3 = [10,20,30]
print(f"1在函数外调用函数前值:{list3},地址{id(list3)}")
change_list(list3)
print(f"4在函数外调用函数后值:{list3},地址{id(list3)}")