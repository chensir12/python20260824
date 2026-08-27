"""
    该案例演示了元组
"""
from operator import length_hint

# 创建元祖
tup1 = (100,200,300,'1234')
tup2 = (100,)
print(tup1,type(tup1))
print(tup2,type(tup2))

# 通过推导式的方式创建元组
# 得到生成器对象
tup_gen = (i for i in range(101))
# 讲生成器对象封装为一个元祖对象
print(tup_gen,type(tup_gen))
tup1 = tuple(tup_gen)
print(tup1)
print(tuple(i for i in range(101)))

# 访问元组中的元素
print(tup1[2])
print(tup1[2:109])

# 元组相加
tuple1 = (100,200,300)
tuple2 = ('a','b','c')
print(tuple1+tuple2)

# 元组乘法
tuple2 = ("a","b","c")
print(tuple2 * 2)

# 成员运算
print(2 not in (1,2,3))

# 获取元组长度
tuple2 = ("a","b","c")
print(len(tuple2))

tuple1 = (100, 200, 300)
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))

# 元组遍历
tuple1 = (100, 200, 300)
# 直接遍历
# for item in tuple1:
#     print(item)

for i in range(len(tuple1)):
    print(tuple1[i])

# enumrate
for i,val in enumerate(tuple1):
    print(i,val)

# 元组的不可变
tup1 = (100, 200, 300)
print(tup1,id(tup1))
tup1 = tup1+(100, 200, 300)
print(tup1,id(tup1))

# 如果元组中元素是可变数据类型，其嵌套项可以被修改
tup1 = (100, 200, 300,[10,20,30])
print(tup1,id(tup1))
tup1[3].append(40)
print(tup1,id(tup1))