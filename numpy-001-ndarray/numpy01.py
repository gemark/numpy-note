import numpy as np

# 创建ndarray的方法
arr1 = np.array([1, 3, 5, 7, 9])  # 通过 python 的 list 创建
arr2 = np.array((2, 4, 6, 8, 10)) # 通过 python 的 tuple 创建
arr3 = np.arange(5) # 这是通过 numpy 的 arange 函数创建
arr4 = np.linspace(0, 2 * np.pi, 5) # 3.1415 * 2
arr5 = np.linspace(0, 100, 6)
print(type(arr1))
print(len(arr4))
print(arr4[len(arr4) - 1])

for i in reversed(range(len(arr4))):
    print('{:.2f}'.format(arr4[i]))