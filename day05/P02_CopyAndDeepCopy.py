"""
    该案例演示了深拷贝，内部可变对象也拷贝了
"""
import copy


def change_list(list1):
    print(f"在函数体中修改前list1：{list1},id：{id(list1)}")
    list1[3].append(400)
    print(f"在函数体中修改后list1：{list1},id：{id(list1)}")
list2 = [1,2,3,[10,20,30]]
print(f"在函数体外修改前list2：{list2},id：{id(list2)}")
# 浅拷贝
# change_list(list2.copy())
# change_list(list.copy(list2))
# change_list(list2[:])
# change_list(copy.copy(list2))
# 深拷贝
change_list(copy.deepcopy(list2))
print(f"在函数体外修改后list2：{list2},id：{id(list2)}")
