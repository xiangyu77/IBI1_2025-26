import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients

print(f"Number of patients: {num_patients}")
print(f"Mean heart rate: {mean_hr:.2f} bpm")

# Categorize
low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif hr <= 120:
        normal += 1
    else:
        high += 1

print(f"\nLow (<60 bpm): {low}")
print(f"Normal (60–120 bpm): {normal}")
print(f"High (>120 bpm): {high}")

# Find largest category
if low >= normal and low >= high:
    largest = "Low"
elif normal >= low and normal >= high:
    largest = "Normal"
else:
    largest = "High"
print(f"\nLargest category: {largest}")

# Pie chart
sizes = [low, normal, high]
labels = ['Low (<60)', 'Normal (60–120)', 'High (>120)']
colors = ['lightcoral', 'lightskyblue', 'gold']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Heart Rate Category Distribution')
plt.axis('equal')
plt.show()
