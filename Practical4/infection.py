# 感染模拟程序
# 1. 设置初始感染人数（例如5）
# 2. 设置每日增长率（例如40%，即0.4）
# 3. 设置总人数（例如91）
# 4. 初始化天数计数器为0
# 5. 当感染人数小于总人数时，循环：
#     显示当前天数和感染人数
#     计算新感染人数 = 当前感染人数 * 增长率
#     更新感染人数 = 当前感染人数 + 新感染人数
#     天数加1
# 6. 循环结束后，显示总天数和最终感染人数# 感染模拟程序
initial_infected = 5   # 初始感染人数
growth_rate = 0.4      # 每日增长率（40%）
total_population = 91  # 班级总人数

infected = initial_infected
days = 0

print("Day 0: infected =", infected)

while infected < total_population:
    days += 1
    new_infections = infected * growth_rate
    infected = infected + new_infections
    print("Day", days, ": infected =", infected)

print("It took", days, "days to infect all", total_population, "students.")