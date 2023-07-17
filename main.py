# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import time
import io
import datetime as dt

"""
print的用法说明：
print('my son %s is %d years old' % (s, a))
'my son %s is %d years old' 这部分叫做：格式控制符
% (s, a)这部分叫做：转换说明符
% 字符，表示标记转换说明符的开始
"""
s = "Jerry"
a = 10
print('My son is %s. He is %d years old' % (s, a))  # my son Jerry is 10 years old
"""
将默认的换行结尾符号，修改为“*”结尾符
"""
print("I", end="*")  # 不换行打印
print("love", end="*")
print("you", end="*")
print("\n")  # I*love*you*

print("I love you \
,you love me")  # "\"行连接符，表示下一行是这行的连续

'''
python的对象有三个属性：ID，type，value
python里所有的变量都是对象
id():查看id，type()查看类型，变量名查看value
'''
print("the id of 'a' is %d" % (id(a)))  # the id of 'a' is 140706945295432
print("the type of 'a' is %s" % (type(a)))  # the type of 'a' is <class 'int'>
print("the value of 'a' is %d" % a)  # the value of 'a' is 10

'''
python的变量类型：
int
float
boolean
string
'''
# int
a = 3
print("the variable of a:(%d),(%s),(%d)" % (id(a), type(a), a))  # the variable of a:(140706945295208),(<class 'int'>),(3)

# float
b = 3.14
print('the variable of b:(%d),(%s),(%d)' % (id(b), type(b), b))  # the variable of b:(2657512687088),(<class 'float'>),(3)

# bool
c = True
print("the variable of c:(%d),(%s),(%d)" % (id(c), type(c), c))  # the variable of c:(140706943769448),(<class 'bool'>),(1)

# string
d = 'Jerry'
print("the variable of d:(%d),(%s),(%s)" % (id(d), type(d), d))  # the variable of d:(2657511233072),(<class 'str'>),(Jerry)

'''
链式赋值和系列解包赋值
'''
x = y = 123
a, b = 2, 3
print(x, y, a, b)  # 123 123 2 3
a, b = b, a  # 互换变量非常方便
print("变量互换", x, y, a, b)  # 变量互换 123 123 3 2

'''
i = 12
print(i)
del(i)
print(i)
'''

'''
时间
'''
print(int(time.time()) / 3600 / 24 / 365 + 1970)  # time.time()得到的结果是现在距离1970年多少秒
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))  # 转义字符年月日用小写，时间用大写
print(time.strftime("%H:%M:%S", time.localtime()))  # 转义字符年月日用小写，时间用大写
print(time.strftime("%M:%S", time.localtime()))  # 转义字符年月日用小写，时间用大写

'''
python的运算符
1、算术运算符：+、 -、 *、 /、 **、 //、 %
2、逻辑运算符： and 、or、 not
3、同一运算符：is 、not is
4、常用的函数：int(),float(),round(),chr(),ord()
5、比较运算符 <,>,<=,>=,==,!=,可以连用 3 < a <10
6、位逻辑运算符  &，|，^(异或) 
7、位移符号 >>,<<
8、运算符的优先级：位运算和算术运算>比较运算符>赋值运算符>逻辑运算符；乘除优先加减
'''
e = 3.5
print("%1.2f四舍五入是%d" % (e, round(e)))  # 四舍五入 3.50四舍五入是4
print("%1.2f取整是%d" % (e, int(e)))  # 取整 3.50取整是3

print("the char of 65 is:%s" % chr(65))  # the char of 65 is:A
print("the ascII of A:%d" % ord("A"))  # the ascII of A:65
print("trans int to float", float(a))  # trans int to float 3.0
print("求商", 7 // 2)  # 求商 3
print("求余", 7 % 2)  # 求余 1

x = 12
y = 5
a = 1
b = 2
F = (5+10*x)/5-13*(y-1)*(a+b)/x+9*(5/x+(12+x)/y)
print("运算结果：F={0:*>12.5f}".format(F))


'''
这个版本的python里已经没有过去【-5，+）的限制了
'''
f = 60
g = 60
print(f is g)  # True

# ********************************************************
#         string:字符串的本质就是字符序列，序号从0开始
# ********************************************************
str1 = "string"
print(str1.center(30, "*"))
h = "  this is a testing Message  "
print(len(h))
print(h.__len__())
print(h.center(50, '*'))  # 中间对齐"**********  this is a testing message  ***********"
print(h.ljust(50, "*"))  # 左对齐"  this is a testing message  *********************"
print(h.rjust(50, "*"))  # 右对齐"*********************  this is a testing message  "
print(h.find("h"))
print(h.rfind("h"))
print(h.strip(" "))  # 删除字符串两端的空格
print(h.rstrip(" "))  # 删除字符串右边的空格
print(h.lstrip(" "))  # 删除字符串左边的空格
print(h.strip(" ").endswith("age"))  # 用于判断字符串后缀是否是某几个字符串，返回值为布尔类型bool
print(h.strip(" ").startswith("this"))  # 用于判断字符串开头是否是某几个字符串，返回值为布尔类型bool
print(h.strip(" ").capitalize())  # This is a testing message
print(h.strip(" ").title())  # This Is A Testing Message
print(h.strip(" ").upper())  # THIS IS A TESTING MESSAGE
print(h.strip(" ").lower())  # this is a testing message
print(h.strip(" ").swapcase())  # THIS IS A TESTING mESSAGE
print("ab""cd")  #abcd
str1 = "abc"
str2 = "def"
print(str1 + str2)  # abcdef
print(str1 * 20)  # abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc
# a = input("输入一个数值")  # input输入的是一个字符串
# print(type(a))

# 转义字符 \r\n\t\\...
str1 = "I\nlove\nyou"
print(str1)
'''
I
love
you
'''
str1 = "I\tlove\tyou"
print(str1)  # I	love	you

# str() [] replace()函数
a = 5.20
print(type(str(a)))  # str()将其他类型转换成字符串
a = "abcdefghijklmnopqrstuvwxyz"
print(a[0])  # a
print(a[25])  # z
print(a[-1])  # z
print(a[-2])  # y
print(a[-26])  # a,逆向是以-1开始

b = a.replace("c", "云")  # ab云defghijklmnopqrstuvwxyz
print(b)

# 字符串切片slice操作
# 存在头尾的参数时，包头不包尾
print(a[:])  # abcdefghijklmnopqrstuvwxyz
print(a[:10])  # abcdefghij
print(a[1:10])  # bcdefghij
print(a[:10:2])  #acegi
print(a[-3:])  # xyz
print(a[-10:-1])  # qrstuvwxy 从倒数10到倒数1
print(a[::-1])  # 倒着取zyxwvutsrqponmlkjihgfedcba

# split()字符串分割join()字符串合并
a = "to be or not to be"
b = a.split(" ")  # ['to', 'be', 'or', 'not', 'to', 'be']
print(b)
c = "*".join(b)  # to*be*or*not*to*be,需要性能的时候最好使用join
print(c)

# 做个练习比较用“+”拼接符连接字符串和用“join”链接字符串那个的性能好
t1 = time.time()
for i in range(100000):
    str1 = str1 + "hi"  # 这种代码效率太低，一定不能使用
t2 = time.time()
print("+耗时：" + str(t2 - t1))  # +耗时：0.1868896484375

str1 = []
t3 = time.time()
for i in range(100000):
    str1.append("hi")  # <--append效率高很多
t4 = time.time()
print("join耗时：" + str(t4-t3))  # join耗时：0.003004789352416992

# 字符串的比较
# 字符串驻留机制，在这个版本里使用所有字符串。原来是只支持符合符号规则的字符串
a = "刘海云"
b = "刘海云"
print(a is b)
print(id(a))
print(id(b))

# 成员操作符
a = "abcdefghijk"
print("abc" in a)  # "abc"在字符串a里面吗
print("cba" not in a)

# 其他方法 isalnum();isalpha();isdigit();isspace();isupper();islower();
# format格式化字符
'''
*********************************************************************
                          format 的用法
*********************************************************************
'''
a = "I am {0}. I works in {1}."
b = a.format('haven', 'citech')  # 生成了一个新字符串，要重新赋值
print('format string: ', b)  # format string:  I am haven. I works in citech.

a = "i am {name}. i works at {company}"
b = a.format(name = 'haven', company = 'citech')
print("format string: ", b)  # format string:  I am haven. I works at citech.
# 填充和对齐：^,<,>:分别表示居中，左对齐，右对齐

a = "i am {0:*^11}. i works at {1:#>10}."
b = a.format("haven", "citech")
print("alignment format:", b)  # 结果：alignment format: i am ***haven***. i works at ####citech.

# 数值格式化
pi = 3.1415926
love = 5201314
print("{0:.2f}".format(pi))
print("{0:0>2f}".format(love))
print("{0:0>10d}".format(love))
print("{0:0<10d}".format(love))
print("{0:0^10d}".format(love))
print("{0:*>10d}".format(love))
print("{0:*<10d}".format(love))
print("{0:*^10d}".format(love))  # "*"表示填充的字符，"^,<,>"：表示对齐位置，10:表示填充后的总字符数，"d,f":表示数据类型。
print("{0:,}".format(love))

# 可变字符串
# 字符一旦生产不可修改，如要生产可变字符串需要使用io模块
Str = "abcdefg"
ioStr = io.StringIO(Str)
print("the ioStr is: ", ioStr)  #the ioStr is:  <_io.StringIO object at 0x00000213AB463370>
print(ioStr.getvalue())  # abcdefg
print()
ioStr.seek(6)
ioStr.write("H")
print(ioStr.getvalue())  # abcdefH

