import numpy as np

# 从data.csv中载入数据到numpy数组中
arr = np.genfromtxt('./data.csv', delimiter=',')
data = arr[1:, :]  # 去除掉field name占用的第一行

# 通过列中的均值，填充nan缺失部分
def fill_non_by_column_mean(t):
    for i in range(t.shape[1]): # i 的意义在于 列数 的迭代
        nan_num = np.count_nonzero(t[:, i][t[:, i] != t[:, i]])
        if nan_num > 0:
            cur_col = t[:, i]
            cur_col_not_nan_sum =cur_col[np.isnan(cur_col) == False].sum()
            effective_col_mean = cur_col_not_nan_sum / (t.shape[1] - nan_num)
            cur_col[np.isnan(cur_col)] = effective_col_mean
            t[:, i] = cur_col
        
# 调用函数整理数据表中的缺失值
fill_non_by_column_mean(data)
# 输出
print(data)