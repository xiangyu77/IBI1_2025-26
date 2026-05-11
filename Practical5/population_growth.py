import matplotlib.pyplot as plt

# Population data (millions)
pop_2020 = {'UK': 66.7, 'China': 1426, 'Italy': 59.4, 'Brazil': 208.6, 'USA': 331.6}
pop_2024 = {'UK': 69.2, 'China': 1410, 'Italy': 58.9, 'Brazil': 212.0, 'USA': 340.1}

percent_change = {}
for country in pop_2020:
    change = (pop_2024[country] - pop_2020[country]) / pop_2020[country] * 100
    percent_change[country] = change
    print(f"{country}: {change:.2f}%")

# Sort descending
sorted_items = sorted(percent_change.items(), key=lambda x: x[1], reverse=True)

print("\nPopulation changes from largest increase to largest decrease:")
for country, change in sorted_items:
    print(f"{country}: {change:.2f}%")

largest_increase = sorted_items[0]
largest_decrease = sorted_items[-1]
print(f"\nLargest increase: {largest_increase[0]} ({largest_increase[1]:.2f}%)")
print(f"Largest decrease: {largest_decrease[0]} ({largest_decrease[1]:.2f}%)")

# Bar chart
countries = [item[0] for item in sorted_items]
changes = [item[1] for item in sorted_items]
colors = ['green' if c >= 0 else 'red' for c in changes]

plt.bar(countries, changes, color=colors)
plt.xlabel('Country')
plt.ylabel('Population change (%)')
plt.title('Population Change 2020–2024')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()