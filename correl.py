# Path setting
import os
from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/KISS_COUNT')
os.listdir()
import pandas as pd
from scipy.stats import pearsonr

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 建立 race_group 數值欄位
group_mapping = {
    'group A': 1,
    'group B': 2,
    'group C': 3,
    'group D': 4,
    'group E': 5
}
df['race_group'] = df['race/ethnicity'].map(group_mapping)

# 欲計算的欄位組合
columns = ['math score', 'reading score', 'race_group']
results = []

# 計算所有兩兩組合的 Pearson 相關係數與 p-value
for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        x = columns[i]
        y = columns[j]
        r, p = pearsonr(df[x], df[y])
        results.append({
            'Variables': f'{x} vs {y}',
            'Pearson r': r,
            'p-value': p,
            'Sample Size': len(df)
        })

# 結果轉為 DataFrame 並輸出
result_df = pd.DataFrame(results)
print(result_df)

import pandas as pd
from scipy.stats import pearsonr

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 建立 race_group 數值欄位（如果還沒做過）
group_mapping = {
    'group A': 1,
    'group B': 2,
    'group C': 3,
    'group D': 4,
    'group E': 5
}
df['race_group'] = df['race/ethnicity'].map(group_mapping)

# 指定要分析的族群
group_labels = ['group A', 'group B', 'group C', 'group D', 'group E']

# 儲存結果用的列表
results = []

# 每一個族群都計算 math vs reading 的 Pearson r 與 p-value
for group in group_labels:
    subset = df[df['race/ethnicity'] == group]
    if len(subset) > 1:
        r, p = pearsonr(subset['math score'], subset['reading score'])
        results.append({
            'Group': group,
            'Pearson r (math vs reading)': r,
            'p-value': p,
            'Sample Size': len(subset)
        })

# 轉為 DataFrame 並輸出結果
result_df = pd.DataFrame(results)
print(result_df)

import pandas as pd
from scipy.stats import pearsonr

# 讀取 Excel 檔案
file_path = 'data_score_race.xlsx'
df = pd.read_excel(file_path)

# 建立 race_group 數值欄位
group_mapping = {
    'group A': 1,
    'group B': 2,
    'group C': 3,
    'group D': 4,
    'group E': 5
}
df['race_group'] = df['race/ethnicity'].map(group_mapping)

# 定義條件與對應的變數組合
conditions = {
    "math score >= 80 (reading vs race_group)": (df[df['math score'] >= 80], 'reading score', 'race_group'),
    "reading score >= 80 (math vs race_group)": (df[df['reading score'] >= 80], 'math score', 'race_group'),
    "math score < 60 (reading vs race_group)": (df[df['math score'] < 60], 'reading score', 'race_group'),
    "reading score < 60 (math vs race_group)": (df[df['reading score'] < 60], 'math score', 'race_group'),
}

# 計算相關係數與 p-value
results = []

for label, (subset, x_col, y_col) in conditions.items():
    if len(subset) > 1:
        r, p = pearsonr(subset[x_col], subset[y_col])
        results.append({
            "Group": label,
            "Pearson r": r,
            "p-value": p,
            "Sample Size": len(subset)
        })

# 顯示結果
result_df = pd.DataFrame(results)
print(result_df)