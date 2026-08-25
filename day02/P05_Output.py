"""
    该案例演示了输出操作
"""
"""
# end 控制了输出结尾
print("hello",end="\n")
print("world")
"""
"""
# 格式化输出
# （1）字符串中使用 % 占位
int1 = 30
float1 = 3.14
str1 = "int1 = %d,float1 = %.2f"%(int1,float1)
print(str1)
"""
"""
# （2）字符串.format()
int1 = 30
float1 = 3.14
# 方式1：不设置指定位置，按默认顺序
str1 = "int1={},float1={}".format(int1,float1)
print(str1)

# 方式2：设置指定位置，不能和方式1混合使用
str1 = "int1={1},float1={0}".format(int1,float1)
print(str1)

# 方式3：设置参数
str1 = "int1={aa},float1={bb}".format(aa=int1,bb=float1)
print(str1)
"""
"""
# 数字的格式化
float1 = 31415.9
str2 = "{:*^20_.2f}".format(float1)
print(str2)
str2 = "{:*<20,.2f}".format(float1)
print(str2)
str2 = "{:*>20,.2f}".format(float1)
print(str2)
"""

# （5）f-字符串
int1 = 30
float1 = 3.14
str1 = f"int1={int1},float1={float1}"
print(str1)

str3 = f"{int1=},{float1=}"
print(str3)

# 使用｛｝来转义大括号
print("{0}对应的位置是{0}".format("hello"))
print("{}对应的位置是｛｛0｝｝".format("hello"))

