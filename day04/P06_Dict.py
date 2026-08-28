"""
    该案例演示了字典
"""
# 创建字典对象
dic1 = {}
dic2 = dict()
dic3 = {"name":"chj","age":30,"gender":"男人"}
dic4 = dict(name="chj",age="30",gender="男人")
dic5 = dict((("name","chj"),("age","22"),("gender","man")))
dic6 = dict([("name","chj"),("age","22"),("gender","man")])
dic7 = dict({("name","chj"),("age","22"),("gender","man")})
print(f"type(dic1) = {type(dic1)}:{dic1}")
print(f"type(dic2) = {type(dic2)}:{dic2}")
print(f"type(dic3) = {type(dic3)}:{dic3}")
print(f"type(dic4) = {type(dic4)}:{dic4}")
print(f"type(dic5) = {type(dic5)}:{dic5}")
print(f"type(dic6) = {type(dic6)}:{dic6}")
print(f"type(dic7) = {type(dic7)}:{dic7}")

# 通过key访问字典中的元素的value
# 可通过 [] 访问字典中的元素。key不存在时会报错
# 也可以通过get()获取字典中的元素。key不存在时会返回None，也可以指定默认值
dic1 = {"name":"chj1","age":30,"gender":"男人"}
print(dic1["name"])
print(dic1.get("name"))
print(dic1.get("high","18cm"))

# 对字典中的元素进行添加或者修改  如果key不存在：添加   如果key存在：修改
dic2 = {"name":"chj2","age":31,"gender":"男人"}
dic2["high"] = "18cm"
dic2["gender"] = "male"
print(dic2)

# 成员运算 只能检查key是否在字典中，不能对值进行判断
print("chj" in dic2)

# 遍历
dic = {"唐僧":"迟重瑞","悟空":"六小龄童","八戒":"马德华","沙和尚":"闫怀礼"}

# 遍历所有的key
for k in dic.keys():
    print(k)
# 遍历所有value
for v in dic.values():
    print(v)
# 遍历k，v
for k,v in dic.items():
    print(k,v)
for k in dic.keys():
    print(k,dic[k])

# 删除字典元素

del dic["八戒"]
print(dic)
# del dic
dic.clear()
print(dic)

# 常用函数
# del dict[key]	根据key删除键值对
# dict.pop(key[,default])	获取key所对应的value，同时删除该键值对，可设置默认值
dic = {"唐僧":"迟重瑞","悟空":"六小龄童","八戒":"马德华","沙和尚":"闫怀礼"}
print(dic.pop("八戒","嫦娥"))
print(dic)
print(dic.pop("c","嫦娥")) # 如果没有默认值并且没有key 那就会报错

# dict.popitem()	取出字典中的最后插入的键值对，字典为空则报错
print(dic.popitem())
# dict.clear()	清空字典
# dict1.update(dict2)	将dict2中的键值对更新到dict1中
dic1 = {"a":1,"b":2,"c":3}
dic2 = {"d":11,"e":22}
dic1.update(dic2)
print(dic1)
# dict.get(key[,default])	        获取字典中key对应value，可设置默认值
# dict.setdefault(key[,default])	获取字典中key对应value，可设置默认值。若key不存在于字典中，将会添加key并将value设为默认值
print(dic1.setdefault("aa",10))
print(dic1)

# dict.keys()	获取字典所有的key，返回一个视图对象。字典改变，视图也会跟着变化
# dict.values()	获取字典所有的value，返回一个视图对象
# dict.items()	获取字典所有的(key,value)，返回一个视图对象
# dict.copy()	拷贝字典
dic3 = dic1.copy()
print(dic1,id(dic1))
print(dic3,id(dic3))

# dict.fromkeys(seq[,default])	以序列seq中元素做字典的key创建一个新字典，可设置value的默认值
list1 = ['a','b','c']
dic = dict.fromkeys(list1,10)
print(dic)

