"""
    该案例演示了一个递归
    求一个整数n的阶乘！ 5*4*3*2*1
"""
# 循环
var = 1
for i in range(1,5+1):
    var *= i
    print(var)

def get_Factorial(n):
    res = 1
    for i in range(n,0,-1):
        res *= i
    return res
print(get_Factorial(5))

# 递归实现
def get_Factorial1(i):
    if i == 1:
        return 1
    return i*get_Factorial(i-1)
print(get_Factorial1(5))