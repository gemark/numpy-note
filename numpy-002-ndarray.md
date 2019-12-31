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



​	

​	





