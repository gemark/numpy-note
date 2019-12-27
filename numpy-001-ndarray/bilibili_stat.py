import numpy as np
import sys, loadcsv, re

loader = loadcsv.loadcsv()
data = loader.load_from_file('./planguage_unfix.csv')

# 创建 ndarray 对象
fix_dataA = []
fix_dataB = []
for row in data:
    if row[2] != '"vkchow"':
        try:
            play_num = float(row[4])
        except:
            play_num = 0.0
        fix_dataA.append(play_num)
        fix_dataB.append(row[6])

arrA = np.array(fix_dataA)
arrB = np.array(fix_dataB)

years = set()
for i in arrB:
    d:str = i.split('/')[0]
    if re.match(r'\d+', d) is not None:
        if len(d) == 4 and d.find('.') == -1:
            years.add(d)
years = list(years)
years.sort()

print(years)
        