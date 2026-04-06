import matplotlib.pyplot as plt

# 给定的心率列表
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 患者数量
num_patients = len(heart_rates)

# 平均心率
mean_hr = sum(heart_rates) / num_patients

print(f"数据集中共有 {num_patients} 名患者。")
print(f"平均心率为：{mean_hr:.2f} bpm")
# 初始化计数器
low = 0
normal = 0
high = 0

# 遍历每个心率值
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif hr <= 120:   # 注意：60-120 包含60和120，所以用 <=120
        normal += 1
    else:
        high += 1

print(f"低心率 (<60): {low} 人")
print(f"正常心率 (60-120): {normal} 人")
print(f"高心率 (>120): {high} 人")
# 将类别和人数放入字典，方便比较
categories = {'低心率': low, '正常心率': normal, '高心率': high}
largest_category = max(categories, key=categories.get)
largest_count = categories[largest_category]

print(f"人数最多的类别是：{largest_category}，共有 {largest_count} 人。")
# 准备数据和标签
sizes = [low, normal, high]
labels = ['低心率 (<60)', '正常心率 (60-120)', '高心率 (>120)']
colors = ['lightcoral', 'lightskyblue', 'gold']

# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('心率类别分布')
plt.axis('equal')  # 保证饼图是圆形
plt.show()
