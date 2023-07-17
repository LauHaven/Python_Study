# 控制语句
# 判断结构
# 在选择和循环结构中，条件表达式为False的情况如下：
# False,0,0.0,None,空序列对象（(),[],{},'',"",空range对象,空迭代对象）
# 其他情况均为True
# --------------------------------------------------------------
# 单分支选择结构
a = 5
if a >= 3:
    print("{0}大于等于3".format(a))

# 双分支结构
if a >= 6:
    print("{0}大于等于6".format(a))
else:
    print("{0}小于6".format(a))

# 三分支结构
a = 80
if a >= 90:
    print("分数是{0}，等级为A".format(a))
elif a >= 80:
    print("分数为{0}，等级为B".format(a))
else:
    print("分数为{0}，等级为C".format(a))

# 多分支结构
a = 75
if a >= 90:
    print("分数是{0}，等级为A".format(a))
elif a >= 80:
    print("分数为{0}，等级为B".format(a))
elif a >= 70:
    print("分数为{0}，等级为C".format(a))
else:
    print("分数为{0}，等级为D".format(a))

# 三元条件运算符
a = "我是True的结果" if 3 < 5 else "我是False的结果"
print("三元条件运算的结果:", a)

# 练习
level = "ABCDEF"
a = int(input("请输入你的成绩： "))
if a < 0 or a > 100:
    print("分数大小超出范围，请重新输入。")
else:
    print("分数为{0}，等级为{1}".format(a, level[9 - a // 10]))

for x in range(6):
    print(x, end="\t")  # 0	1	2	3	4	5
print("\n")
for x in range(1, 6):  # 1	2	3	4	5
    print(x, end="\t")

print("\n")
print("-------------------------------")
for i in range(5):
    for j in range(5):
        print(i, end="\t")
    print()

print("--------------string-----------------")
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0} X {1} = {2} ".format(i, j, i * j), end="\t")
    print()

print("---------------[]----------------")
s = []
for i in range(1, 10):
    for j in range(1, i + 1):
        s.append("{0} X {1} = {2}".format(i, j, i * j))
    print("\t".join(s))
    s = []

while True:
    s = input("请输入一个字符（输入Q或者q时推出循环）：")
    if s.upper() == "Q":
        break
    else:
        print("你当前输入的字符是：", s)
print("退出循环成功")

d1 = dict(name="G1", salary=10000, city="beijing")
d2 = {"name": "G2", "salary": 20000, "city": "Shanghai"}
d3 = dict([("name", "G3"), ("salary", 30000), ("city", "shenzhen")])
tb = [d1, d2, d3]
for d in tb:
    print(d)

print("the salary is more than 15000: ")
n = 0
max_salary = 0
sum_salary = 0
for d in tb:
    sum_salary += d["salary"]
    if d["salary"] >= 15000:
        n += 1
        if d["salary"] > max_salary:
            max_salary = d["salary"]
        print(d)
print("总人数为{3}人，平均工资为：{2}元,工资大于15000元的有：{0}人，其中最高工资为：{1}元".format(n, max_salary,
                                                                                             sum_salary / len(tb),
                                                                                             len(tb)))
n = 0
salary = []
while True:
    s = input("请输入工资(q/Q退出)：")
    if s.upper() == "Q": break
    if not s.isdigit():
        print("工资必须是数字，请重新输入")
        continue
    else:
        if int(s) < 0:
            print("工资不能为负数，请重新输入")
            continue
        n += 1
        salary.append(int(s))

print("总人数：", len(salary))
print("最高工资为", max(salary))
print("总工资数:", sum(salary))
print("平均工资为", sum(salary) / len(salary))

# 循环中的else语句
s = ""
ss = 0
for i in range(4):
    s = input("input a number('Q' or 'q' to exit)")
    if s.upper() == "Q":
        break
    else:
        ss += i
else:
    print("get 4 number")

# 循环代码的优化
# 1、尽量减少循环内部不必要的计算
# 2、嵌套循环中，尽量减少内层循环的计算，尽可能向外提
# 3、局部变量查询速度快，尽量使用局部变量

# 并行迭代zip
name = ["G1", "g2", "G3"]
age = [18, 19, 20]
job = ['engineer', 'student', 'teacher']
for n, a, j in zip(name, age, job):
    print("{0}-{1}-{2}".format(n, a, j))
