"""
    该案例演示了异常处理
"""
# 没有进行异常处理，如果发生异常后，程序中断，后面的代码不会执行
# res = 3 / 0
# print(res)
# print("end")

try:
    res = 3 / 0
except:
    print("除数不能为0")

print("end")