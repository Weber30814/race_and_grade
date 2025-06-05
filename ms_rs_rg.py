# Path setting
import os
from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/KISS_COUNT')
os.listdir()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取 Excel 資料
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 設定 Seaborn 圖表風格
sns.set(style="whitegrid")

# 散佈圖 1: math score vs reading score
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='math score', y='reading score', hue='race_group', palette='Set2')
plt.title('Math Score vs Reading Score')
plt.show()

# 箱型圖 2: math score vs race_group
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='race_group', y='math score', palette='Set2')
plt.title('Math Score by Race Group')
plt.show()

# 箱型圖 3: reading score vs race_group
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='race_group', y='reading score', palette='Set2')
plt.title('Reading Score by Race Group')
plt.show()