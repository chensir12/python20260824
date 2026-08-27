"""
    晨测题
"""
# 编写一个程序，从 1 循环到 10，当数字是偶数时打印 “偶数”，奇数时打印 “奇数”
for i in list(range(11))[1:]:
    if i % 2 == 0:
        print(f'{i}是偶数')
    else:
        print(f'{i}是奇数')

# 现有列表 my_list = [10, 20, 30, 40, 50]，请编写代码实现：
my_list = [10, 20, 30, 40, 50]
#  向列表末尾添加一个元素 60。
my_list.append(60)
print(my_list)
# 取出列表中索引为 2 的元素。
print(my_list[2])
# 计算列表中所有元素的和。
print(sum(my_list))

# 使用for循环，打印如下图形的*
#    *
#   ***
#  *****
# *******
#*********

for i in range(5):
    str1 = ' '*(4-i)+'*'*(2*i+1)+' '*(4-i)
    print(str1)

n=5
for i in range(1,n + 1):
    for k in range(0,n - i):
        print(" ",end="")

    for j in range(1,2 * i):
        print("*",end="")
    print()