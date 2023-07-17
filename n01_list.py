# the new file of python for chapter 3
import random


print("hello citech haven")

print("-------------- list -----------------")
# 序列结构
# 序列类型：字符串、列表、元组、字典、集合
# list的大小可变，根据需要随时增加或缩小
a = [10, 20, "abc", True]
print(id(a))
print(type(a))
print(id(a[0]))
print(type(a[0]))
print(id(a[2]))
print(type(a[2]))

# 基本语法【】创建
a = [1, 2, "haven", "citech"]  # 对象的类型可以不同
b = []  # 空列表

# list()创建,可以将任何可迭代的数据转化成列表
a = list()  # 创建一个空列表
b = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list b:", b)
c = list("haven and citech")
print("list c:", c)  # ['h', 'a', 'v', 'e', 'n', ' ', 'a', 'n', 'd', ' ', 'c', 'i', 't', 'e', 'c', 'h']

# range()创建整数列表 range([start,] end [,step])
d = range(1, 10, 2)
print(list(d))
d = range(-3, 20, 3)
print(list(d))

# 推导式生成列表
a = [x*2 for x in range(10)]
print(a)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
a = [x*2 for x in range(100) if x % 9 == 0]  # 先用for循环生成数据，再用if语句进行过滤
print(a)  # [0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]

# 列表元素的增加和删除
# 我们一般只在列表的最后增删，这会大大提高列表的操作效率
a = [10, 20, 30]
print(id(a))
a.append(40)
print(a)
print(id(a))

# 使用“+”运算符会产生新的列表
a = [10, 20, 30]
print(a)
print(id(a))  # 2365326495552
a = a + [40, 50]
print(a)
print(id(a))  # 2365327368320

# extend方法不会产生新的列表，推荐使用该方法
a = [10, 20, 30]
print(a)
print(id(a))  # 1622120795968
a.extend([40, 50])
print(a)
print(id(a))  # 1622120795968

# insert插入元素，原来的元素位置会完后移动,不会产生新列表
a = [1, 2, 3, 4]
print(id(a))  # 2255221842048
a.insert(3, 5)
print("插入新元素：", a)
print(id(a))  # 2255221842048

# 乘法扩展列表,不会产生新列表
a = [1, 2, 3]
print(id(a))  # 1586883596096
a = a*3
print("用乘法扩展列表", a)
# print(id(a))  # 1586884469056
#
# del列表元素的删除,其后的元素向前移动，不会产生新列表
# insert和del操作都会涉及元素拷贝，效率较低，尽量少用
a = [1, 2, 3]
print(id(a))  # 2456708714304
del(a[1])
print(a)
print(id(a))  # 2456708714304

# pop弹掉最后一个元素,不会产生新列表
a = [1, 2, 3, 4]
print(id(a))  # 1525294391616
b = a.pop()
print(a)
print(id(a))  # 1525294391616
print(b)

# pop弹掉指定元素，不会产生新列表
a = [1, 2, 3, 4]
print(id(a))  # 2402055556160
b = a.pop(2)  # 如果形参为空，在弹掉最后一个元素
print(a)
print(id(a))  # 2402055556160
print(b)

# remove 删除首次出现的指定元素，做不存在元素抛出异常
a = [1, 2, 3, 4]
print(id(a))  # 1734276243776
a.remove(2)
print(a)
print(id(a))  # 1734276243776

'''
a = [1, 2, 3, 4]
print(id(a))  # 1734276243776
a.remove(5)
print(a)
print(id(a))  # 1734276243776
'''
# 通过索引直接访问元素
a = [1, 2, 3, 4, 5, 5, 6, 5]
b = a[2]
c = a[1:3]  # 包头不包尾
print(b, " ", c)

# index获取首次出现的元素的索引值
d = a.index(4)
print(d)  # 出现在3的位置
d = a.index(4, 2)
d = a.index(4, 2, 4)

# len返回元素数量
print("元素个数： ", len(a))

# 成员资格判断
# count判断列表中是否存在指定元素，0：无，大于0有。但用in更简洁
print(a)
if a.count(5) > 0:  # 元素是‘5’的数量大于0个
    print("存在")
    print("count: ", a.count(4))  # 1
else:
    print("不存在")

# 着这种方式判断更简洁
print(4 in a)
print(6 in a)

# 列表的slice切片操作【偏移start:偏移end:步长step】
b = a[:]
print(b)
b = a[1:3]  # 包头不包尾
print(b)
b = a[1:6:2]
print(b)
b = a[-7:-3:2]  # 包头不包尾
print(b)
b = a[::-1]
print(b)  # [5, 6, 5, 5, 4, 3, 2, 1]

# 列表遍历
for x in a:
    print(x)

# 列表元素的排序
a = [3, 2, 7, 4, 6]
print(id(a))  # 2109263122624
a.sort()  # [2, 3, 4, 6, 7]
print(a)
a.sort(reverse=True)
print(a)
print(id(a))  # 2109263122624
random.shuffle(a)
print("random list", a)
print(id(a))  # 2109263122624

# 列表的迭代器 reversed,产生了一个指针，指向列表的最后，然后一个一个的往前移动，迭代器只能使用一次
print(a)
b = reversed(a)
print(type(b))  # <class 'list_reverseiterator'>
c = list(b)
print("第一次使用迭代器b：", c)
c = list(b)
print("第二次使用迭代器b：", c)

# list的一些小方法：max,min,sum
print("max:", max(a))
print("min:", min(a))
print("sum:", sum(a))

# 多维列表
# 一维列表可以帮助我们存储一维的线性的数据
# 二位列表可以帮助我们存储二维的表格的数据
a = [
    ["gao1", 18, 30000, "beijing"],
    ["gao2", 19, 20000, "shanghai"],
    ["gao3", 20, 10000, "shenzhen"]
]
print(a)  # [['gao1', 18, 30000, 'beijing'], ['gao2', 19, 20000, 'shanghai'], ['gao3', 20, 10000, 'shenzhen']]
print(a[0])  # ['gao1', 18, 30000, 'beijing']
print(a[0][0])  # gao1
print(" --- 遍历二维列表里做有对象的值：--- ")
for m in range(len(a)):
    for n in range(len(a[0])):
        print(a[m][n], end="\t")
    print(" ")
'''
 --- 遍历二维列表里做有对象的值：--- 
gao1
18
30000
beijing
 
gao2
19
20000
shanghai
 
gao3
20
10000
shenzhen
'''

