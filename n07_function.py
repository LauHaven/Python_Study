# function
import math
import time

print("-------------- function ----------------")


# python 函数的分类：
# 1、内置函数
# 2、标准库函数
# 3、第三方库函数
# 4、用户自定义函数
# def 函数名
# “文档字符串”
# 函数体
# 要点：
# 1、我们使用def来定义函数，然后就是一个空格和函数名称
# 1.1、python执行def时，会创建一个函数对象，并绑定到函数名变量上。
# 2、参数列表
# 2.1、圆括号内是参数列表，有多个参数则使用逗号隔开
# 2.2、形式参数不需要声明类型，也不需要指定函数返回类型
# 2.3、无参数，也必须保留空的圆括号。
# 2.4、实参列表必须与形参列表一一对应。
# 3、return返回值
# 3.1、如果函数体中包含return语句，则结束函数执行并返回值
# 3.2、如果函数体中不包含return语句，则结束函数时返回None
# 4、调用函数之前，必须先定义函数，即先调用def创建函数对象
# 4.1、内置函数对象会自动创建
# 4.2、标准库和第三方库函数，通过import导入模块时，会执行模块中的def语句。

def func01():
    print("my first function")


print(id(func01))
print(type(func01))
func01()
for a in range(3):
    func01()


# 形参和实参
def get_max(a, b):
    """用于比较两个数的大小，并将大的一个打印出来"""
    if a > b:
        print(a, "比较大")
    if a < b:
        print(b, "比较大")
    if a == b:
        print("一样大")


get_max(2, 6)
get_max(5, 3)
get_max(5, 5)
help(get_max.__doc__)


# 返回值
def print_star(n, t):
    s = str(t)
    if (n - len(s)) % 2 != 0:
        m = n - 1
    else:
        m = n
    print(s.center(len(s) + 2, " ").center(m, "*"))


print(print_star(40, "返回值"))


def avg(a):
    return sum(a) / len(a)


print_star(40, "avg")
print(avg([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def double_list(a):
    b = [x * 2 for x in a]
    return b


print_star(40, "double_list")
print(double_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 函数也是对象，内存底层分析
print_star(40, "函数也是对象，内存底层分析")


def test():
    print("citech")


c = test
print(type(c))
print(id(test))
print(id(c))
c()  # 小括号表示调用的意思
test()

# 局部变量和全局变量
a = 10


def double_a():
    global a  # 如果没有声明为全局变量，这”a“被认为时局部变量，不会修改全局变量”a“的值
    a = 20
    print(a)


double_a()
print(a)


def global_list():
    k = list(globals().keys())
    v = list(globals().values())
    print()
    print("本模块共有{0}个全局变量。详细列表如下：".format(len(k)))
    print("-" * 60)
    for i in range(len(k)):
        print('"{0}": '.format(k[i]).ljust(25, " "), "\t", v[i])


global_list()

# 测试一下函数使用全局变量和局部变量的效率
print_star(40, "函数使用全局变量和局部变量的效率")


def test01():
    start = time.time()
    for i in range(100000000):
        math.sqrt(30)
    end = time.time()
    print("耗时{0}：".format(end - start))


test01()


def test02():
    start = time.time()
    b = math.sqrt
    for i in range(100000000):
        b(30)
    end = time.time()
    print("耗时{0}：".format(end - start))


test02()

print_star(40, "函数")
# 20230718 第一次使用Github管理代码。
