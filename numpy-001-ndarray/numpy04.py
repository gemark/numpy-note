import numpy as np

# create empty ndarray (2d)
a = np.arange(25)      # create 1D array
a = a.reshape((5, 5))  # one Dismensional reshape to twd D

"""
a:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
"""

b = np.array([10, 62, 1, 14, 2, 
              56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 
              43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print(a.dtype)
print(b.dtype)

# basic operator
print(a + b)    # add
print(a - b)    # sub
print(a * b)    # mul
print(b / a)    # div
print(a ** b)   # pow
print(a > b) # show True or False in orignal structor
print(a < b)
print(a.dot(b))

print(a.sum()) # 300
print(b.sum()) # 889 对所有的item进行求和
print(b.min()) # 找出该数组中的最小的一个元素
print(b.max()) # 找出该数组中的最大的一个元素
c = b.cumsum()
print(c)
print(len(c))