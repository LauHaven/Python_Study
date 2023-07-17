print("\
*********************************************************\n\
*                  Tuple:   元组\n\
*********************************************************\n\
")
# 元组属于不可变序列
# 元组支持的操作：索引访问、切片、连接、成员关系、比较运算，len(),max(),min(),sum()等
a = (10, 20, 30)
print(type(a))  # <class 'tuple'>
a = 10, 20, 30  # 可以不用小括号
print(type(a))  # < class 'tuple'>
a = tuple("I love python")
print(a)
a = tuple(range(5))
print(a)
a = tuple([1, 2, 3, 4])  # package
print(a)
print(type(a))
a = (10)
print(type(a))  # <class 'int'>
a = (10,)
print(type(a))  # <class 'tuple'>

# del a  # 删除一个元组
a = (1, 2, 3, 4, 5, 6)
b = a[1:3]
print(b)  # (2, 3)
b = a[:4]
print(b)  # (1, 2, 3, 4)
b = a[:]
print(a)
b = a[::2]
print(b)

b = sorted(a)
print(b)  # [1, 2, 3, 4, 5, 6],**注意 - 生成了列表

a = tuple(b)
print(a)
print(a + tuple(b))

# zip 将多个列表对应的位置的元素组合成为元组，并返回这个zip对象
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
d = zip(a, b, c)  # can be used only one time
print(id(d))  # 2173326806720
print(type(d))  # <class 'zip'>
print(d)  # <zip object at 0x000001FA045F4EC0>

f = tuple(d)
print("first time to use the zip", f)  # first time to use the zip ((1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12))

e = list(d)
print("second time to use the zip", e)  # second time to use the zip []

# 生成器推导式创建元组
a = (2 ** x for x in range(11) if x > 0)  # can be used one time only
print(tuple(a))  # an tuple object (0, 1, 2, 3, 4)
print(list(a))  # an empty object []

a = (2 ** x for x in range(5) if x > 0)  # can be used one time only
b = a.__next__()
print(b)
b = a.__next__()
print(b)
b = a.__next__()
print(b)
b = a.__next__()
print(b)
# b = a.__next__()
# print("end=", b)  # 打印不出来

#  1、元组的核心特点：不可变序列；
#  2、元组的访问和处理速度比列表快；
#  3、与整数和字符串一样，元组()可以作为字典的键，列表[]则永远不能作为字典的键使用。
