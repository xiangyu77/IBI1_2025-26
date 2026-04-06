# 2004年苏格兰人口（百万）
a = 5.08
# 2014年苏格兰人口
b = 5.33
# 2024年苏格兰人口
c = 5.55

# 计算2004-2014年的变化
d = b - a
# 计算2014-2024年的变化
e = c - b

# 比较两个变化量
if d > e:
    print("2004-2014年增长更快")
elif d < e:
    print("2014-2024年增长更快")
else:
    print("两个十年增长相同")

# 判断人口增长是加速还是减速
if e > d:
    print("人口增长正在加速")
else:
    print("人口增长正在减速或保持不变")
# 布尔变量练习
X = True
Y = False

W = X or Y   # W 等于 X 或 Y 的逻辑或结果

# 打印不同组合下的W值
print("X=True, Y=False -> W=", W)
print("X=True, Y=True -> W=", (True or True))
print("X=False, Y=True -> W=", (False or True))
print("X=False, Y=False -> W=", (False or False))

# 真理表注释
# or 运算的真值表：
# True or True = True
# True or False = True
# False or True = True
# False or False = False