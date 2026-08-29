"""
    该案例演示了return
"""
def print_start():
    print("*"*20)
    return
print_start()

# 两数求和
def sum(num1, num2):
    res = num1 +num2
    return res
aa =sum(1,2)
print(aa)

def sum(num1,num2):
    res = num1 + num2
    print(res)
print(sum(1,2))

# return返回多个值 多个值会放在一个元组里
def func(a,b,c):
    return a,b,c,[a,b,c]

print(func(1,2,3))

def func():
    for i in range(10):
        if i == 5:
            # return 直接结束整个函数
            # pass 就是一个占位填充的作用 没有实际意义
            # continue
            break
        print(f"当前i的值是{i}")
    print("这是循环体外部")
func()