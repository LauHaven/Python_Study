print("\
**************************************\n\
*          dictionary  字典           *\n\
**************************************")

# 字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值对”，包含：“键对象”和“值对象”
# 可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。
# 列表中我们通过“下标数字”找到对应的对象。字典中通过“键对象”找到对应的“值对象”。“键”是任意的不可变数据，比如：整数、浮点数、字符串、元组。
# 但是：列表、字典、集合这些可变对象是甭能作为“键”。并且”键“不可重复。“值”可以是任意的数据，并且可重复。

# 字典的创建，几种定义方式
#  1、{}和dict创建
# “：”创建
a = {"name": "haven", "age": 29, "job": "engineer"}
print(id(a))
print(type(a))
print(a)

# “=”创建
b = dict(name="haven", age=29, job="engineer")  # 注意这里用dict()
print(id(b))
print(type(b))
print(b)

# “[()]”创建
c = dict([("name", "haven"), ("age", 29), ("job", "engineer")])
print(id(c))
print(type(c))
print(c)

#  zip
k = ["name", "age", "job"]
v = ["haven", 29, "engineer"]
d = dict(zip(k, v))  # 第一个参数是键，第二个参数是值
print("d=", d)  # d= {'name': 'haven', 'age': 29, 'job': 'engineer'}

# 通过fromkeys创建键值为空的字典
a = dict.fromkeys(["name", "age", "job"])  # 注意使用list[]创建一个值为空的字典
print("a=", a)  # {'name': None, 'age': None, 'job': None}
print("items: ", d.items())  # 所有键和值
print("keys:", d.keys())  # 所有键
print("values:", d.values())  # 所有值

# 字典的访问
print(d)
print(d["name"])  # haven
# print(d["works"])  # error
print(d.get("name"))  # haven
print(d.get("works"))  # 不存在的键，则返回None
print(d.get("works", "不存在"))  # 如果没有该键值，默认返回"不存在"
print(len(d))
a = "name" in d
print(a)

# 字典元素的添加、修改、删除
d["address"] = "东莞"
print(d)
d["age"] = 30
print(d)
e = {"name": "Jerry", "age": 18, "sex": "male"}
d.update(e)  # 用字典e的值来更新d，d和e同时存在的键，用e键值替代d中对应键的键值；d不存在而e存在的键和键值，添加到d中
print("update result:", d)
del (d["sex"])
print(d)
h = d.pop("address")
print(h)
print(d)
d.clear()
print(d)

d = {'name': 'Jerry', 'age': 18, 'job': 'engineer', 'address': '东莞', 'sex': 'male'}
print(d)  # {'name': 'Jerry', 'age': 18, 'job': 'engineer', 'address': '东莞', 'sex': 'male'}
d.popitem()
print(d)  # {'name': 'Jerry', 'age': 18, 'job': 'engineer', 'address': '东莞'}
d.popitem()
print(d)  # {'name': 'Jerry', 'age': 18, 'job': 'engineer'}
d.popitem()
print(d)  # {'name': 'Jerry', 'age': 18}
d.popitem()
print(d)  # {'name': 'Jerry'}

# 序列解包
x, y, z = 10, 20, 30
print("1: x={0},y={1},z={2}".format(x, y, z))  # 10 20 30
x, y, z = (10, 20, 30)
print("2: x={0},y={1},z={2}".format(x, y, z))  # 10 20 30
(x, y, z) = (10, 20, 30)
print("3: x={0},y={1},z={2}".format(x, y, z))  # 10 20 30
x, y, z = [10, 20, 30]
print("4: x={0},y={1},z={2}".format(x, y, z))  # 10 20 30
[x, y, z] = [10, 20, 30]
print("5: x={0},y={1},z={2}".format(x, y, z))  # 10 20 30

d = {'name': 'Jerry', 'age': 18, 'job': 'engineer', 'address': '东莞', 'sex': 'male'}
print(d)
# x, y, z = "name", "age", "job"
# x, y, z = d
# print("6: x={0},y={1},z={2}".format(x, y, z))

# 练习

d = {"name": ["gao1", "gao2", "gao3"], "age": [18, 19, 20], "city": ["beijing", "shanghai", "shenzhen"]}
print(d["name"][0])
print(d["name"][1])
print(d.get("name")[2])
print("----------- name -----------")
for i in range(len(d)):
    print(d.get("name")[i])
print("----------- table -----------")
print("name\tage\tcity")
print("-------------------")
for i in range(len(d)):
    print("{0}\t{1}\t{2}".format(d.get("name")[i], d.get("age")[i], d.get("city")[i]))

d1 = {"name": "gao1", "age": 18, "city": "beijing"}
d2 = {"name": "gao2", "age": 19, "city": "shanghai"}
d3 = {"name": "gao3", "age": 20, "city": "shenzhen"}
d = [d1, d2, d3]
print(d)
print(d[1].get("name"))

# 字典用法总结：
# 1、键必须是可散列的
# （1）、数字、字符串、元组都是可散列的。
# （2）、自动逸对象需要支持下面三点：
#      a、支持hash()函数
#      b、支持通过__eg__()方法检测相等性
#      c、若a==b时，则hash（a)==hash(b)也为真
# 字典在内存中国开销巨大，典型的空间换时间
# 键查询的速度很快
# 往字典里添加新建可能导致扩容，导致散列表中键的次序变化。因此，不要咋遍历字典的同时进行字典的修改。
# 如果一个对象是可散列的，那么在这个对象的生命周期中，他的散列值是不会变的（它需要实现__hash__()方法）。
# 一般用户自定义的类型的对象都是可散列的，散列值就是它们的id()函数的返回值，所以所有这些对象在比较的时候都是不想等的。

# 集合 集合中的元素时唯一不重复的
a = {1, 2, 3, 4}
a.add(4)
print(a)  # {1, 2, 3, 4},已经存在4，不增加
a.add(5)
print(a)  # {1, 2, 3, 4, 5}，集合中没有5，增加元素
a.remove(3)
print(a)  # {1, 2, 4, 5}
b = [6, 5, 4, 3, 2]
a = set(b)
print(a)  # {2, 3, 4, 5, 6}
b = (4, 5, 6, 7, 8)
a = set(b)
print(a)  # {4, 5, 6, 7, 8}

# 响数学中概念一样，集合也提供并集、交集、差集
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
# 并集
c = a.union(b)  # 把在b中出现但a中出现的元素与a一起放入c
print(c)  # {1, 2, 3, 4, 5, 6, 7}
c = a.intersection(b)  # 把只有同时出现在a和b中的元素放入c
print(c)  # {3, 4, 5}
c = a.difference(b)  # 把只在a中出现，b中没有的元素放入c
print(c)  # {1, 2}
