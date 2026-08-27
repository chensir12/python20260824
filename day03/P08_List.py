"""
    该案例演示了列表
"""
from subprocess import list2cmdline

"""
# 创建列表
list1 = [100,200,300,400,500]
print(list1,type(list1))

# 访问列表中的元素
print(list1[2])
print(list1[-3])

# 切片：从容器中取出部分元素
# 取全部元素
print(list1)
print(list1[:])
# 取索引从2开始到4（不包含的元素）
print(list1[0::2])
# 取索引从2开始到末尾
print(list1[2:])
# 取索引从0开始到2（不包含）的元素
print(list1[0:3])
print(list1[-3:0:-1])
# 取索引从2开始到-1（不包含）的元素
# 倒序取元素
list1.reverse()
print(list1)

# 复制整个列表（内存中指的不是一个地址,类似java的clon）
list2 = list1[:]
list3 = list1
print(id(list2))
print(id(list1))
print(id(list3))
print(list2)
print(list3)
"""
"""
list1 = [100,200,300,400,500]
# 向列表中添加元素
# 在列表的末尾追加元素
list1.append(600)
print(list1)
# 在列表指定的索引位置 添加元素
list1.insert(2,600)
print(list1)
"""
'''
# 列表相加 不是直接在原列表上进行的相加操作，会创建一个新的对象
list1 = [1,2,3]
list2 = ['a','b','c']
print(list1+list2)

# 列表乘法
list1 = [1,2,3]
print(list1 * 2)

#修改列表中的元素
list1 = [1,2,3]
list1[2] = 600
print(list1)
list1[1:4] = ["a","b","c"]
print(list1)

print(10 in list1)
'''
"""
# 获取列表中的元素个数（列表的长度）
list1 = [100,200,300,400,500]
print(len(list1))

print(max(list1))
print(min(list1))
print(sum(list1))
"""
"""
# 遍历列表中的元素
list1 = [100,200,300,400,500]
# 1)直接遍历列表元素
for item in list1:
    print(item)
# 2)通过下标遍历列表
for i in range(len(list1)):
    print(list1[i])

item1 = 0
while item1 < len(list1):
    print(list1[item1])
    item1 += 1

for i,val in enumerate(list1):
    print(i,val)
"""
"""
# 删除列表中的元素
list1 = [100,200,300,300,400,500]
list1.remove(300) # 删除出现的第一个符合的元素
print(list1)
del list1[0]
print(list1)
del list1
# print(list1)

list1 = [100,200,300,300,400,500]
for item in list1[:]:
    if item == 300:
        list1.remove(item)
print(list1)

list1 = [[1,2],[3,4],[5,6]]
print(type(list1))
print(type(list[0]))
for item in list1:
    for i in item:
        print(i,end=' ')
"""
"""
# 列表推导式
list1 = [1,2,3,4,5]

list2 = []
for i in list1:
    list2.append(i * 2)
print(list2)
list2 = [ i * 2 for i in list1 ]
print(list2)
list2 = [i for i in list1 if i % 2 == 0]
print(list2)
list2 = [i for i in list1 if i != 5]
print(list2)

list5 = [1,2,3,4,5]
list6 = ["a","b","c","d","e"]
list7 = []
for i in list5:
    for j in list6:
        list7.append((i,j))
print(list7)
list7 = [(i,j) for i in list5 for j in list6]
print(list7)
"""
list5 = [1,2,3,4,5]
list6 = ["a","b","c","d","e"]
zipeded = zip(list5,list6)
print(list(zipeded))
print(list(zip(list5,list6)))

