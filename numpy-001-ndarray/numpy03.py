import numpy as np

one_d_array = [0, 1, 2, 3, 4, 5]

two_d_array = [
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28 ,29, 30],
    [31, 32, 33, 34, 35]
]

t = one_d_array[3]
#               x: coord(index)

e = two_d_array[2][1]
#               y  x  y:row x:column

arr = np.array(two_d_array) # 将列表转换为 ndarray

# print(arr[2, 2])
# 对一个二维数组的列进行切片
print(arr[1,5:8])
# 对一个二维数组的行进行切片
print(arr[1:, 1:4])
# 控制步进
print(arr[::4,::4])
# 行列转换(有一点丢弃其他部分的意思在里面)
print(arr[1, :])