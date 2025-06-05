# Path setting
import os
from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/KISS_COUNT')
os.listdir()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 設定 Seaborn 圖表風格
sns.set(style="whitegrid")

# 列出所有要處理的 group
groups = ['group A', 'group B', 'group C', 'group D', 'group E']

# 對每個 group 畫圖
for g in groups:
    plt.figure(figsize=(6, 4))
    subset = df[df['race/ethnicity'] == g]
    sns.regplot(data=subset, x='math score', y='reading score', scatter=True, ci=95)
    plt.title(f'Math vs Reading Score - {g}')
    plt.xlabel('Math Score')
    plt.ylabel('Reading Score')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()