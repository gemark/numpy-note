import numpy as np

# 多维问题
three_d_array = [
    [
        [1, 2, 3],  
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [-1, -2, -3],  
        [-4, -5, -6],
        [-7, -8, -9]
    ],
    [
        ['a', 'b', 'c'],  # 访问这里的第二个元素 'b'
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ],
]
b = three_d_array[2][0][1]
#z  y  x

arr = np.array(three_d_array)
print(arr[1,2,2])