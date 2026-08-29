"""
    函数参数的形式
"""
# 必须参数  按位置把每个相应位置的实参和形参进行关联，要求实参的数量和形参的数量必须一致
def func(a,b,c):
    print(a,b,c)
func(1,2,3)

# 关键字参数    按照名称对参数进行关联   要求实参传递的时候指定的名称和形参的名称必须要一致   对顺序没有要求
def print_info(age,name):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
print_info(name = "chj",age = 20)

# 默认值参数   非默认参数必须放在默认参数之前。
# 在调用函数的时候，如果给你默认值参数传递了实参，那么使用传递的值，如果没有传递实参，使用默认值
def print_info1(age,name="chj"):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
print_info1(age = 20)
print_info1(40,name = "xyz")

# 不定长参数
# 形式一：   *参数名    可以接收多个参数，底层是将多个参数放到元组中进行处理
# 注意：在 *var这种形式的不定长参数后，可以加普通参数，但是调用函数的时候，只能通过关键字参数的形式给不定长参数后面的普通参数进行传参
def print_info2(num,*var,age):
    print(num)
    print(var)
    print(age)
print_info2(10, 20 ,age=30)
print_info2(10,age=30)
# print_info(num=30,20,40) 必须参数必须要传不然会报错

# 不定长参数
# 形式二：   **参数名   底层是通过字典对传递的参数进行封装处理
# 注意：如果是两个*的不定长参数，后面不能再出现其他参数了
def print_info3(num,**vardict):
    print(num)
    print(vardict)
print_info3(10,a = 20,b = 30)
# print_info3(10,20,30) 这种不定长参数必须用字典的形式

# 解包传参
def print_info4(a,b,c):
    print(a,b,c)
tup1 = (10,20,30)
print_info4(*tup1)
dic = {"a":10,"b":20,"c":30}
print_info4(**dic)
list1 = [10,20,30]
print_info4(*list1)

# / 前的参数必须使用位置传参，* 后的参数必须用关键字传参。
def print_info5(a,b,/,c,d,e,*,f,g):
    print(a,b,c,d,e,f,g)

print_info5(10,20,30,40,50,f=60,g=70)
print_info5(10,20,30,d=40,e=50,f=60,g=70)


def print_info(num,num1,num2,num3):
    print(num)
    print(num1)
    print(num2)
    print(num3)
print_info(10,20,30,40)
print_info(num = 10,num1=20,num2=30,num3=40)

print_info(10,20,30,num3=40)
print_info(5,num1=10,num3=20,num2=30)

