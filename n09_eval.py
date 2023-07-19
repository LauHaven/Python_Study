# eval函数的功能：将字符串str当成有效的表达式来求值并返回计算结果
# 语法：eval（source[,globals[,locals]]->value
# source:一个python表达式或函数compile()返回的代码对象
# globals:可选，必须时dictionary对象
# locals:可选，任意映射对象

s = "print('I love wendy.')"
eval(s)
a, b = 10, 20
c = eval("a+b")
print(c)

# 分别用几种不通过的dictionary定义方式验证eval函数
d = dict(a=100, b=200)
d1 = {"a": 300, "b": 200}
d2 = dict([("a", 400), ("b", 500)])
print(eval("a+b", d))
print(d1)
print(eval("a+b", d1))
print(eval("a+b", d2))
