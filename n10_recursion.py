# 递归函数recursion

result = 1


def func01(n):
    global result
    if n != 0:
        result = result * n
        n = n - 1
        func01(n)


def func02(n):
    global result
    func01(n)
    s = result
    result = 1
    return s


print('---recursion---')
print("{0}的阶乘：{0}!={1}".format(5, func02(5)))
print("{0}的阶乘：{0}!={1}".format(12, func02(12)))
print("{0}的阶乘：{0}!={1}".format(120, func02(20)))


def func03(n):
    global result
    if n != 0:
        result = result * n
        func03(n - 1)
    if n ==5:
        s = result
        result = 1
        return s

print(func03(5))