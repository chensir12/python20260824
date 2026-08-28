"""
    该案例演示了集合
"""
from traceback import print_tb

from numpy.testing.print_coercion_tables import print_new_cast_table

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

# set.add(x) 添加元素
# set.update(x) 添加元素,x可以为列表、元组、字符串、字典等可迭代对象
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# set.union 添加元素后返回一个新的集合，x可以为列表、元组、字符串、字典等可迭代对象
set3 = {6, 7, 8}
print(set1.union(set3))

# set.remove(x) 从集合中移除x，x不存在则报错
# set.discard(x) 从集合中移除x，x不存在也不报错
# set.pop() 随机取出集合中的一个元素，如果集合为空则报错
# set.clear() 清空集合

# set.difference(x1,...)	求set1和x1的差集，返回一个新的集合
# set.difference_update(x1,...)	求set1和x1的差集

# set.intersection(x1,...)	求set1和x1的交集，返回一个新的集合
# set.intersection_update(x1,...)	求set1和x1的交集
print(set1.intersection_update(set2))
print(set1)

# set1 & set2	两集合求交集
# set1 | set2	两集合求并集
# set1 - set2	两集合求差集

# print(set1.isdisjoint(set2)) 判断两集合是否没有交集
# print(set1.issubset(set2)) 判断set1是否为set2的子集
# print(set1.issuperset(set2)) 判断set2是否为set1的子集
# print(set1.symmetric_difference(set2)) 求两集合中不重复的元素，返回一个新的集合
# set1.symmetric_difference_update(set2) 求两集合中不重复的元素
print(set1)
# set.copy() 拷贝集合
set3 = set1.copy()
set4 = set.copy(set1)
print(set3,id(set3))
print(set1,id(set1))

