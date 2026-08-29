"""
    该案例演示了匿名函数 Lambda 表达式
"""

# 版本1： 写一个两个整数加法的计算器
def calculate(a, b):
    return a + b

print(calculate(2, 3))

# 版本2： 丰富计算器的功能，提供 +  - * /    这种方式 计算逻辑和计算器本身绑定的太死
def calculate(a, b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

print(calculate(2, 3, '*'))

# 版本3： 计算器函数和计算逻辑分开
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

# 函数可以作为参数进行传递
def calculate(a,b,op):
    return op(a,b)

print(calculate(2, 3, add))

# 版本4：  使用lambda匿名函数
def calculate(a,b,op):
    return op(a,b)

print(calculate(10, 20, lambda a, b: a + b))

# 需求：  在当前列表基础上，对每一个元素加一个atguigu前缀，返回一个新的列表
list1 = [10,20,30,40]
# 方式1：列表推导式
list2 = ["atguigu"+str(i) for i in list1]
print(list2)
# 方式2：循环
list2 = []
for i in list1:
    list2.append("atguigu" + str(i))
print(list2)

# 写一个通用的对列表进行处理的函数       传一个列表进行，对列表中的每一个元素进行处理之后  返回一个新的列表  处理逻辑不固定
def my_map(func,list1):
    list2 = []
    for item in list1:
        list2.append(func(item))
    return list2
list3 = [10,20,30,40,50]

def fff(item):
    return item * 2
print(my_map(fff,list3))
print(my_map(lambda item:item * 2,list3))


# sorted 函数
student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
print(sorted(student_list,key=lambda x:x['age']))
# map 函数
list1 = [10,20,30,-1]
result_map = map(lambda x: x * x, list1) #会返回一个新的容器
print(list1)
print(list(result_map))
# filter 函数
filter_result = filter(lambda x:x>0,list1)
print(list(filter_result))
# refuce 函数
from functools import reduce
reduce_result = reduce(lambda x,y:x+y,[1,2,3,4,5])
print(reduce_result)

# 函数的注释
# 1.普通的自定义函数
def dog(name, age, species):
   return (name, age, species)
# 2.带函数注释的函数
def dog(name:str,age:(1,99),species:'狗狗的品种') -> tuple:
    return (name,age,species)
print(dog(10,20,30)) #函数参数注释并不会强制参数的类型
print(dog.__annotations__)
