import numpy as np


list1 = [3, 4, 5, 6, 10, 21]
avg = sum(list1) / len(list1)

print(avg)
print(np.mean(list1))
print(np.median(list1))

mu, sigma = 0.0, 1.0
stock_day_rise = np.random.normal(mu, sigma, [500, 504])

a = stock_day_rise[:2, 0:4]  # 提取1，2两支股票的前四天数据
b = stock_day_rise[10:12, 0:4] # 提取11,12两支股票的前四天数据

print(a)
print(b)

# axis=1时候，按照数组的列方向拼接在一起
# axis=0时候，按照数组的行方向拼接在一起
c = np.concatenate([a, b], axis=0)
print(c)

print("垂直栈：")
print(np.vstack([a, b]))
print("水平栈：")
print(np.hstack([a, b]))

print('分割后：')
print(np.split(a, [3], axis=1)[0])

r = np.random.randint(100, 500)
b = np.random.randint(100, 504)

temp = stock_day_rise[r-100:r, b-100:b]

print('所有四支股票前四天的最大涨幅:{}'.format(np.max(temp, axis=1)))
print('所有四支股票前四天的最小涨幅:{}'.format(np.min(temp, axis=1)))
print('所有四支股票前四天的涨幅均值:{}'.format(np.mean(temp, axis=1)))
std = np.std(temp, axis=1)
print('所有四支股票前四天涨幅标准差:{}'.format(std))
var = np.var(temp, axis=1)
print('所有四支股票前四天的涨幅方差:{}'.format(var))

# 获取股票指定哪一天的涨幅最大
print("前四只股票在100天内涨幅最大{}".format(np.argmax(temp, axis=1)))
print("前100天在天内涨幅最大的股票{}".format(np.argmax(temp, axis=0)))

new_arr = np.array([1, 3, 10, 11, 0, 2])
print(np.argmax(new_arr))

students_score = np.array([
    [80,86],
    [82,80],
    [85,78],
    [90,90],
    [86,82],
    [82,90],
    [78,80],
    [92,94]
])

students_score_mat = np.mat(students_score) # numpy中matrix必须是二维的
print(np.matmul(students_score, np.array([[0.7], [0.3]])))

# print(stduents_score * np.array([0.3, 0.7]))

# 数组与数的运算
arr = np.array([[1,2,3,2,1,4], [5,6,1,2,3,1]])
print(arr + 1)
print(arr / 2)

# 数组与数的运算中，当一个一维数组乘以3
a = [1,2,3,4,5]
print(a * 3) # 类似于字符串的乘法
print('abc'*3) # 对于数组的乘法，相当于重复repeat

# arr1 = np.array([[1,2,3,2,1,4], [5,6,1,2,3,1]])
# arr2 = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])

arr1 = np.array([[1, 2, 3, 2], [5, 6, 1, 2]])
arr2 = np.array([[1, 2], [3, 2]]) # 4x4 cant mul 2x2

# print(arr1 * arr2) # 两个数组相乘时，shape必须一致

arr3 = np.array([[5], [4]]) # 可以相乘 4x4 mul 2x1 its ok
print(arr1 * arr3)

arr4 = np.array([2]) # 4x4 mul 1x1 its ok
print(arr1 * arr4)

