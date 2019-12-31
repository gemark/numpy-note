## 股票涨跌幅数据案例

```python
# 两年504天，500支股票
# 0 表示均值 μ
# 1 表示方差 σ
stock_day_rise = numpy.random.normal(0, 1, [500, 504])
```

![正态分布](assets/正态分布.png)

正态分布是一种概率分布。正态分布是具有两个参数μ和σ的连续型随机变量的分布，第一参数μ是服从正态分布的随机变量的均值，第二个参数σ是此随机变量的方差，所以正态分布记作**N(μ，σ )**。

**生活、生产与科学实验中很多随机变量的概率分布都可以近似地用正态分布来描述。**

**μ决定了其位置，其标准差σ**。决定了分布的幅度。当μ = 0,σ = 1时的正态分布是标准正态分布。

```python
# 改变股票数组的行和列形状（504为天数，500为股票数量）
stock_day_rise.reshape([504, 500])
stock_day_rise.resize([504,500])
```

```python
# 修改小数为整数的int32
stock_day_rise.reshape([504, 500]).astype(np.int32)
# 对小数位数进行修改，这里修改为只有4位
np.round(stock_day_rise[:2, :20], 4)
```



## 常用的ndarray的访问方式（多维切片）：

```python
# 访问第10到100支股票的， 100到150天的涨跌幅数据
print(stock_day_rise[99:150, 9:100])
print(stock_day_rise[:, 98])
print(stock_day_rise[::2, 9])
```



## numpy统计运算

| 统计方法     | 描述                    |
| ------------ | ----------------------- |
| numpy.max()  | 统计数组中最大的item    |
| numpy.min()  | 统计数组中最小的item    |
| numpy.mean() | 统计数组中items的均值   |
| numpy.var()  | 统计数组中items的方差   |
| numpy.std()  | 统计数组中items的标准差 |
| numpy.cov()  | 统计矩阵中的协方差      |
| np.argmax()  | 统计最大值的item的索引  |
| np.argmin()  | 统计最小值的item的索引  |



## 运算

```python
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
```

结果：

```python
[[81.8]
 [81.4]
 [82.9]
 [90. ]
 [84.8]
 [84.4]
 [78.6]
 [92.6]]
```

运算例子：

```python
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
```



​	





