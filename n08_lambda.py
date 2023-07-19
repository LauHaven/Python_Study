# lambda表达式和匿名函数

f1 = lambda a, b, c: a + b + c

f2 = [lambda a: a ** 2, lambda a: a ** 3, lambda a: a ** 4]


def test01(a, b):
    return a + b


print(f1(1, 2, 3))
print(f2[0](2), f2[1](2), f2[2](2))
print(test01(1, 2))

# Python中一切皆对象
g = [f1, f2, test01]
print(g[0](1, 2, 3), g[1][2](2), g[2](1, 2))
