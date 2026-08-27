"""
    该案例演示了集合
"""
from traceback import print_tb

# 集合对象的创建
set1 = {1, 2, 3}
list1 = [1, 2, 3]
print(set1,type(set1))
set2 = set(list1)
print(set2)
set3 = set()
print(type(set3))
print(type({}))

# 集合推导式
list1 = [1,2,3,4,5]
set2 = {i * 2 for i in list1}
print(set2)

# 向集合中添加元素
set1 = {1, 2, 3}
print(set1,id(set1))
set1.add(4)
print(set1,id(set1))

# 从集合中删除元素
set1 = {1,2,3}
print(set1,id(set1))
set1.remove(2)
print(set1,id(set1))

# 遍历集合
# 直接遍历
set1 = {1, 2, 3}
for item in set1:
    print(item)

# set.ad(x)
