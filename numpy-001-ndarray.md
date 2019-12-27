## 什么是Numpy

Python的一种科学计算工具



## 为什么使用Numpy

因为它快！



## Numpy的用途

1. 密集的数据计算
2. python自身不擅长的计算(性能问题)



## Numpy中的NDArray

1. 什么是`ndarray`

   n -> 多

   d -> 维度

   array -> 数组

   多维数组（因为numpy的ndarray不是python实现，而是底层语言实现，并对其优化）

2. 创建ndarray的几种方式

   ```python
   import numpy as np
   
   # 利用python的list对象进行创建(列表)
   arr1 = np.array([1, 3, 5, 7, 9])
   # 利用python的tuple对象进行创建(元组)
   arr2 = np.array((2, 4, 6, 8, 10))
   # 利用numpy的arange()函数进行创建
   arr3 = np.arange(10)
   # 利用numpy的linspace()函数进行创建
   arr4 = np.linspace(0, 2 * np.pi, 5)
   
   # 如果我们要对这些ndarray进行输出，可以直接使用python中的print函数
   # 或者使用下标
   ```

   ```python
   import numpy as np
   
   # 创建ndarray的方法
   arr1 = np.array([1, 3, 5, 7, 9])  # 通过 python 的 list 创建
   arr2 = np.array((2, 4, 6, 8, 10)) # 通过 python 的 tuple 创建
   arr3 = np.arange(5) # 这是通过 numpy 的 arange 函数创建
   arr4 = np.linspace(0, 2 * np.pi, 5) # 3.1415 * 2
   arr5 = np.linspace(0, 100, 6)
   print(type(arr1))
   print(len(arr4))
   print(arr4[len(arr4) - 1]) # 通过下标的方式访问（numpy数组支持python语法）
   
   for i in reversed(range(len(arr4))):
       print('{:.2f}'.format(arr4[i]))
   ```

3. 维度

    ![image-20191227102659753](assets/image-20191227102659753.png)
    
    ![image-20191227104654985](assets/image-20191227104654985.png)

```python
# 一维与二维数组的问题
one_d_array = [0, 1, 2, 3, 4, 5]

two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

t = one_d_array[3]
#               x: coord(index)

e = two_d_array[2][1]
#               y  x  y:row x:column
```

```python
# 三维数组的维度问题
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
#                 z  y  x
# 上述代码，由于第3层中的数据是文本类型（str），所以在转换为ndarray后，无法参与正常的运算
# 因为numpy.ndarray是需要保证数组中的所有元素必须是相同的数据类型
```



对于传统数组(python list)的访问：

```python
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
b = three_d_array[2][0][1] # 每一个维度的下标都要填写在[]方括号内
```

对于ndarray却不需要这样做，我们可以简化成这样：

```python
arr = np.array(three_d_array)
print(arr[1,2,2]) # 可以在一个方括号内，完成多个维度下标的填写，用逗号分隔开即可
```

上列代码中[1,2,2]表示我们访问z:1 y:2, x;3(深度、行、列)



## ndarray切片

```python
# MD Array,
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
 
# 对列进行切片 
print(a[0, 2:4]) # [13, 14]
# 对行进行切片
print(a[2:4, 0]) # [21, 26]
# 步进
print(a[::2, ::2]) # [[11, 13, 15], [21, 23, 25], [31, 33, 35]]
# 行列转换(要不就是只要列，要不就是只要行)
print(a[:, 1]) # [12, 17, 22, 27, 32]
```



## ndarray属性

array properties(接上面的二维数组)

```python
print(type(a)) # <class 'numpy.ndarray'>
print(a.size) # 25
print(a.itemsize) # 8
print(a.nbytes) # 200 -> 4bytes(itemsize * size)
print(a.dtype) # 'int64' 64bit integer
print(a.shape) # (5, 5)
print(a.ndim) # 2
```

正如你在上面的代码中看到的，NumPy数组实际上被称为ndarray。我不知道为什么他妈的它叫ndarray，如果有人知道请留言！我猜它代表n维数组 -> (N-dimensional)。

数组的形状是它有多少行和列，上面的数组有5行和5列，所以它的形状是(5，5)。

`itemsize`属性是每个项()占用的字节数。这个数组的数据类型是int 64，一个int 64中有64位，一个字节中有8位，除以64除以8，你就可以得到它占用了多少字节，在本例中是8。

`ndim`属性是数组的维数。这个有2个。例如，向量只有1。

`nbytes` 属性是数组中的所有数据消耗掉的字节数。你应该注意到，这并不计算数组的开销，因此数组占用的实际空间将稍微大一点。



## ndarray的基本操作

```python
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
print(a > b)    # show True or False in orignal structor
print(a < b)
print(a.dot(b)) # vector operator 向量运算（点积）
```

其他操作

```python
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
print(a > b)    # show True or False in orignal structor
print(a < b)
print(a.dot(b))

print(a.sum()) # 300
print(b.sum()) # 889 对所有的item进行求和
print(b.min()) # 找出该数组中的最小的一个元素
print(b.max()) # 找出该数组中的最大的一个元素
c = b.cumsum()
print(c)
print(len(c))
```



## 案例

bilibili -> planguage_unfix.csv





## 杂项
numpy基础作弊表

![python-numpy-basic-cheet-sheet](assets/numpy-basic-cheet-sheet.png)

