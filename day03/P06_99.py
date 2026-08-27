"""
    该案例演示了打印99乘法表
"""

# for i in range(10):
#     j = 1
#     while j < i+1:
#         print(f"{i} * {j} = {i*j}",end=" ")
#         j += 1
#     print()

for i in range(1,10):
    for j in range(1, i+1):
        print(f"{i} * {j} = {i*j}",end="\t")
    print()