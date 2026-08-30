"""
    该案例演示了list中的函数
"""
list1 = [600,100,200,300,400,500,200]
# list.insert(index,x)	在指定位置插入x
# list1.insert(0,30)
# list.append(x)	在列表末尾追加x
# list1.append(600)
# list1.extend(list2)	在列表1的末尾追加列表2的数据
list1.extend([600])
print(list1)

# del list[index]	删除指定位置的数据或切片
list1 = [600,100,200,300,400,500,200]
del list1[0:3]
print(list1)
# list.remove(x)	删除第一次出现的x
list1.remove(200)
# list.pop([index])	删除指定位置的数据，默认为末尾数据
list1 = [600,100,200,300,400,500,200]
print(list1.pop(2))
print(list1)
# list.clear()	清空列表中元素
list1.clear()
print(list1)
# list[index] = x	修改指定位置的数据
# list1[start:end] = list2	修改列表切片的数据
# list1[1] = 555
# list1[0:3] = [11,22,33]
# sorted(list[,reverse=True])	返回排序后的新列表，可选降序
list1 = [600,100,200,300,400,500,200]
print(sorted(list1,reverse=True))
# list.sort([reverse=True])	对列表就地排序，可选降序
print(list1)
list1.sort(reverse=True)
print(list1)
# list.reverse()	反转列表中的元素
list1 = [600,100,200,300,400,500,200]
list1.reverse()
print(list1)
# list.index(x[,start,[,end]])	返回x在列表中首次出现的位置，可指定起始和结束范围
list1 = [600,100,200,300,400,500,200]
# print(list1.index(600,1,3)) #解释型语言错误了就到这里就停下了
print("hello world")
# list.count(x)	返回x的数量
list1 = [600,100,200,300,400,500,200]
print(list1.count(600))
# len(list)	返回列表元素个数
# print(len(list1))
# max(list)	返回列表中最大值
# min(list)	返回列表中最小值
# sum(list)	返回列表中所有元素和
# list.copy()	拷贝列表
# list2 = list[:]
list2 = list1.copy()
print(list2)
# list(x)	将序列转换为列表
aa = range(10)
print(type(aa))
bb = list(aa)
print(bb,type(bb))
print(type((1,2)))