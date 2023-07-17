# 推导式是从一个或者多个迭代器快速创建序列的一种方法。
# 它可以将循环和条件判断结合，从而避免冗长的代码。
# 推导式是典型的python风格。

# 列表推导式
# 语法1；[表达式 for item in 可迭代对象]
# 语法2：[表达式 for item in 可迭代对象 if 条件判断]
a = [x * 2 for x in range(1, 11)]
print(a)
a = [x * 2 for x in range(1, 11) if x % 2 == 0]
print(a)
a = [ord(s) for s in "haven"]
print(a)
a = [chr(a) for a in range(65, 91)]
print(a)
a = [(x, y) for x in range(1, 5) for y in range(1, 3)]
print(a)

# 字典的推导式生成字典对象，格式如下：
# {key_expression：value_expression for 表达式 in 可迭代对象}
# {key_expression: value_expression for 表达式 in 可迭代对象 if 判断条件}
s = "I love you. I love python. I love programme."
cc = {c: s.count(c) for c in s}
print(cc)

cc = {}
for c in s:
    cc[c] = s.count(c)
print(cc)

# 集合推导式
# {key_expression for 表达式 in 可迭代对象}
# {key_expression for 表达式 in 可迭代对象 if 判断条件}

b = {i * 2 for i in range(1, 5)}
print(b)

# 生成器推导式（生成元组）
# 元组没有推导式，通过小括号生成的是“一个生成器对象”，该对象只能使用一次，再使用就没有了。
g = (2 * x for x in range(1, 5))
print(g)  # <generator object <genexpr> at 0x000002133F398040>
a = tuple(g)
print(a)  # (2, 4, 6, 8)

g = (2 * x for x in range(1, 5))
for i in g:
    print(i, end="\t")
for i in g:
    print(i, end="\t")  # 空的
