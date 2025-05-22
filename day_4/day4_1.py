####函数
# def 函数名（参数列表）:
#     函数体

def max(a,b):
    if a>b :
        print(a)
    else:
        print(b)

max(10,99999)
#####一个简单的函数 id()获取变量的地址


# !/usr/bin/python3

# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme( str = "菜鸟教程")#####关键字函数
printme("菜鸟教程")######非关键字参数，，，，二者优劣是非关键字可以更改传入参数的顺序
max(b=30,a=50)###这是一个实例


# !/usr/bin/python3

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


def printinfo_2(arg1, arg2, *var_tuple):
    print("固定参数 1:", arg1)
    print("固定参数 2:", arg2)
    print("可变参数:")
    for var in var_tuple:
        print(var)
printinfo_2(90, 80, 70, 60, 50)###针对printinfo函数的改良版



#    可写函数说明   字典的形式存储
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)########声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：



#########匿名函数结构lambda [arg1 [,arg2,.....argn]]:expression

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
print(mydoubler(11))



# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
#
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
# 以下使用方法是正确的:
#
# f(10, 20, 30, d=40, e=50, f=60)
# 以下使用方法会发生错误:
#
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式

