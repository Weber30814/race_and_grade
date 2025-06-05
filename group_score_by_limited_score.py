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

# 篩選 math score >= 80 的資料
df_high_math = df[df['math score'] >= 80]

# 畫出 race_group vs reading score 的箱型圖
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_high_math, x='race_group', y='reading score', palette='Set2')
plt.title('Reading Score by Race Group (Math Score ≥ 80)')
plt.xlabel('Race Group')
plt.ylabel('Reading Score')
plt.grid(True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 篩選 reading score >= 80 的資料
df_high_reading = df[df['reading score'] >= 80]

# 畫出 race_group vs math score 的箱型圖
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_high_reading, x='race_group', y='math score', palette='Set2')
plt.title('Math Score by Race Group (Reading Score ≥ 80)')
plt.xlabel('Race Group')
plt.ylabel('Math Score')
plt.grid(True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 建立 race_group 數值欄位（如果尚未建立）
group_mapping = {
    'group A': 1,
    'group B': 2,
    'group C': 3,
    'group D': 4,
    'group E': 5
}
df['race_group'] = df['race/ethnicity'].map(group_mapping)

# 篩選 reading score < 60 的資料
df_low_reading = df[df['reading score'] < 60]

# 畫出 race_group vs math score 的箱型圖
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_low_reading, x='race_group', y='math score', palette='Set2')
plt.title('Math Score by Race Group (Reading Score < 60)')
plt.xlabel('Race Group')
plt.ylabel('Math Score')
plt.grid(True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 建立 race_group 數值欄位（如尚未建立）
group_mapping = {
    'group A': 1,
    'group B': 2,
    'group C': 3,
    'group D': 4,
    'group E': 5
}
df['race_group'] = df['race/ethnicity'].map(group_mapping)

# 篩選 math score < 60 的資料
df_low_math = df[df['math score'] < 60]

# 畫出 race_group vs reading score 的箱型圖
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_low_math, x='race_group', y='reading score', palette='Set2')
plt.title('Reading Score by Race Group (Math Score < 60)')
plt.xlabel('Race Group')
plt.ylabel('Reading Score')
plt.grid(True)
plt.show()
