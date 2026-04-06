import matplotlib.pyplot as plt

# 2020年人口（单位：百万）
pop_2020 = {
    'UK': 66.7,
    'China': 1426,
    'Italy': 59.4,
    'Brazil': 208.6,
    'USA': 331.6
}

# 2024年人口
pop_2024 = {
    'UK': 69.2,
    'China': 1410,
    'Italy': 58.9,
    'Brazil': 212.0,
    'USA': 340.1
}
# 创建一个字典存储变化百分比
percent_change = {}

for country in pop_2020:
    p2020 = pop_2020[country]
    p2024 = pop_2024[country]
    change = ((p2024 - p2020) / p2020) * 100
    percent_change[country] = change

print("各国人口变化百分比：")
for country, change in percent_change.items():
    print(f"{country}: {change:.2f}%")
    # 按百分比变化降序排序
sorted_countries = sorted(percent_change.items(), key=lambda item: item[1], reverse=True)

print("\n人口变化从大到小排序：")
for country, change in sorted_countries:
    print(f"{country}: {change:.2f}%")
    # 最大增加的国家（排序后的第一个）
largest_increase_country = sorted_countries[0][0]
largest_increase_value = sorted_countries[0][1]

# 最大减少的国家（排序后的最后一个）
largest_decrease_country = sorted_countries[-1][0]
largest_decrease_value = sorted_countries[-1][1]

print(f"\n人口增长最大的国家：{largest_increase_country}，增长 {largest_increase_value:.2f}%")
print(f"人口减少最大的国家：{largest_decrease_country}，变化 {largest_decrease_value:.2f}%")
# 提取国家和变化值（按原顺序或排序后均可，这里用排序后的顺序使条形图更清晰）
countries = [item[0] for item in sorted_countries]
changes = [item[1] for item in sorted_countries]

# 设置颜色：正值为绿色，负值为红色
colors = ['green' if c >= 0 else 'red' for c in changes]

plt.bar(countries, changes, color=colors)
plt.xlabel('国家')
plt.ylabel('人口变化百分比 (%)')
plt.title('2020-2024年各国人口变化')
plt.axhline(0, color='black', linewidth=0.8)  # 添加一条水平线在0处
plt.show()