"""
    该案例演示了字符串常用的函数
"""
from traceback import print_tb

str1 = "hello world"
# str.replace(old,new[,max]) 将字符串中的old替换成new，如果指定max，则替换不超过max次
str2 = str1.replace("h","1")
print(str2)

# str.split([x][,n]) 按x分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数
str1 = "id,name,age,gender"
print(str1.split(",",2))
# str.rsplit([x][,n]) 与split()类似，从右边开始分隔
print(str1.rsplit(",",2))

# x.join(seq) 以x作为分隔符，讲序列中所有字符串合并为一个新的字符串
print("_".join(["1","2","3","4","5"]))
print("_".join(("1","2","3","4","5")))
print("_".join('12345'))

# str.strip([x]) 截掉字符串两边的空格或指定字符
str1 = "xxxhelloxxxx"
print(str1.strip().strip("x"))
#  str.lstrip([x]) 截掉字符串左边的空格或指定字符
print(str1.lstrip("x"))
#  str.rstrip([x]) 截掉字符串右边的空格或指定字符
print(str1.rstrip("x"))

# str.removeprefix() 截掉字符串指定前缀
print("str.removeprefix() 截掉字符串指定前缀:",str1.removeprefix("xxx"))

# str.removesuffix() 截取字符串指定后缀
print(str1.removesuffix("xxxx"))

# str.upper() 将所有字符转为大写
print("hello".upper())
# str.lower() 将所有字符串转为小写
print("HELLO".lower())

# str.swapcase() 反转字符串中字母大小写
print("hello WORLD".swapcase())

# str.capitalize() 讲字符串中第一个字母变为大写，其他字母变为小写
print("hello".capitalize())

# str.title() 将字符串每个单词首字母大写
print("hello world".title())

# str.casefold() 返回适合无大小写比较的字符串版本
print("helLO World".casefold())

# len(str)	返回字符串长度
# print(len("hello"))
# max(str)	返回字符串中最大值
print(min("healloz"))
# min(str)	返回字符串中最小值

# str.find(x[,start][,end])	返回字符串中第一个x的索引值，不存在则返回-1，可指定字符串开始结束范围
print("helloh".find('h',2))
# str.rfind(x[,start][,end])	与find()类似，从右边开始查找
print("hello".rfind('h'))

# str.index(x,[,start][,end]) 返回字符串中第一个x的索引值，不存在则报错，可指定字符串开始结束范围
print("hello".index('h'))
# str.rindex(x[,start][,end])	与index()类似，从右边开始查找

# str.count(x[,start][,end]) 返回字符串中x的个数，可指定字符串开始结束范围
print('abcdefghijklmmmmn'.count("m"))

# str.startwith(x[,start][,end]) 检查字符串是否以x开头，可指定字符串开始结束范围
print("hello".startswith("at"))

# str.endswith(x[,start][,end]) 检查字符串是否以x结尾，可指定字符串开始结束范围
print("hello".endswith("o"))

# str.isspace() 检查字符串是否非空且只包涵空白
print("   ".isspace())

# str.isalnum()	检查字符串是否非空且只包含字母(英文字母+汉字)和数字
print("hello123!***".isalnum())
# str.isalpha()	检查字符串是否非空且只包含字母(英文字母+汉字)
print("hello你哄啊".isalpha())
# str.isascii() 检查字符串是否只包含ASCII字符，空字符串也是ASCII
print("hello ".isascii())
# str.isdecimal()
print("1234 ".isdecimal())
# str.isdigit()
print("1234".isdigit())
# str.isnumeric()
print("12345".isnumeric())