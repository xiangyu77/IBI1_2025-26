import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\20590\Desktop\新建文件夹 (4)\IBI1_2025-26\Practical10")

print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))

dalys_data.info()
print(dalys_data.describe())

subset_iloc = dalys_data.iloc[0:10, 2:4]
print(subset_iloc)

afghan_data = dalys_data.loc[dalys_data['Entity'] == "Afghanistan"]
afghan_first10 = afghan_data.iloc[0:10]
max_row = afghan_first10.loc[afghan_first10['DALYs'].idxmax()]
max_year = max_row['Year']
print(f"Afghanistan max DALYs in first 10 years: {max_year}")

is_zimbabwe = dalys_data['Entity'] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]
print(f"Zimbabwe data years: {zimbabwe_years.min()} to {zimbabwe_years.max()}")

data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]
max_row_2019 = data_2019.loc[data_2019['DALYs'].idxmax()]
max_country = max_row_2019['Entity']
min_row_2019 = data_2019.loc[data_2019['DALYs'].idxmin()]
min_country = min_row_2019['Entity']
print(f"Highest DALYs in 2019: {max_country}")
print(f"Lowest DALYs in 2019: {min_country}")

country_data = dalys_data.loc[dalys_data['Entity'] == max_country, ['Year', 'DALYs']]
plt.figure(figsize=(8,5), dpi=150)
plt.plot(country_data['Year'], country_data['DALYs'], 'b-', marker='o', markersize=3)
plt.xlabel('Year')
plt.ylabel('DALYs per 100,000 people')
plt.title(f'DALYs over time in {max_country}')
plt.grid(True)
plt.savefig(f'{max_country}_DALYs_trend.png')
plt.show()

# Own question: distribution of DALYs in 2019
data_2019_daly = dalys_data.loc[dalys_data['Year'] == 2019, 'DALYs']
plt.figure(figsize=(6,4), dpi=150)
plt.hist(data_2019_daly, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('DALYs per 100,000')
plt.ylabel('Number of countries')
plt.title('Distribution of DALYs across countries in 2019')
plt.savefig('DALYs_histogram_2019.png')
plt.show()