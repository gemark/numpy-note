import numpy as np
import datetime, sys, pymysql, time

list1 = [1, 2, 3, 4, 5]
total = sum(list1)
avg = total / len(list1)
print(avg)

# zero = np.zeros([3, 3], dtype=np.uint8)
# print(zero[0, :])
# print(zero.ndim)
# print(zero.shape)
# print(zero.dtype)

# list2 = np.array(list1, dtype=np.float)
# print(list2.dtype)
# print(list2)

# a = np.array([[1,2,3],[4,5,6]])
# # 从现有的数组当中创建
# a1 = np.array(a)
# # 相当于索引的形式，并没有真正的创建一个新的
# a2 = np.asarray(a)

# print(a2)

# ls = np.logspace(0, 100, num=10)
# print(ls)

""" 
int8    signed      -2^(8-1) ~ 2^(8-1) - 1
int16   signed      -2^(16-1) ~ 2^(16-1) - 1
int32   signed      -2^(32-1) ~ 2^(32-1) - 1
int64   signed      -2^(64-1) ~ 2^(64-1) - 1
uint8   unsigned    0 ~ 2^8 - 1
uint16  unsigned    0 ~ 2^16 - 1
uint32  unsigned    0 ~ 2^32 - 1
uint64  unsigned    0 ~ 2^64 - 1
"""

# simple:np.ndarray = np.array([4, 1, 5, 6, 9, 7])
# m = simple.mean() # 均值
# v = simple.var()  # 方差
# s = simple.std()  # 标准差
# mi = simple.min() # 获取最小值
# mx = simple.max() # 获取最大值
# print(m)
# print(v)
# print(s)
# print(mi)
# print(mx)

def GeneratorDate(s_year, s_month, s_day, e_year, e_month, e_day, exculdeWeekday=True) -> list:
    start_year = s_year
    start_month = s_month
    start_day = s_day
    date_list = []
    while True:
        try:
            d = datetime.date(start_year, start_month, start_day)
            start_day += 1
            if exculdeWeekday:
                if d.isoweekday() == 6 or d.isoweekday() == 7:
                    if d.year == e_year and d.month == e_month and d.day == e_day:
                        break
                    continue
            date_list.append(d)
            if d.year == e_year and d.month == e_month and d.day == e_day:
                break
        except ValueError:
            err_info = str(sys.exc_info()[1])
            if err_info[:3] == 'day':
                start_day = 1
                start_month += 1
            if err_info[:3] == 'mon':
                start_month = 1
                start_year += 1
    return date_list

stock_day_rise:np.ndarray = np.random.normal(0, 1, (1631, 522))
date_list: np.ndarray = np.array(GeneratorDate(2018, 1, 1, 2019, 12, 31))

stock_list = []
try:
    conn = pymysql.Connect('localhost', 'root', 'vkchow', 'bilibili')
    cur:pymysql.cursors.Cursor = conn.cursor()
    row = 1631
    if row % 100 == 0:
        page_num = row / 100
    else:
        page_num = row // 100 + 1
    for i in range(page_num):
        sql = 'select * from new_stock_final limit {0}, {1}'.format(
            i * 100,
            100
        )
        cur.execute(sql)
        data = cur.fetchall()
        for v in data:
            stock_list.append(list(v))

    print(len(stock_list))
    conn.close()
except:
    sys.exit(1)

stock_final = []
count = 0
for row in stock_day_rise:
    date_count = 0
    for col in row:
        num = stock_list[count][0]
        name = stock_list[count][1]
        d = date_list[date_count]
        rise = col
        stock_final.append([num, name, d, rise])
        date_count = date_count + 1
    count = count + 1

print('链接数据库...')
try:
    conn = pymysql.Connect('localhost', 'root', 'vkchow', 'bilibili')
    print('数据库链接成功')
    start = time.time()
    print('开始执行数据库写入')
    # 获取游标
    cur: pymysql.cursors.Cursor = conn.cursor()
    # 游标执行excute(sql语句)
    count = 1
    for v in stock_final:
        if count % 100 == 0:
            conn.commit()
            print('已提交：{}条'.format(count))
        sql = 'insert into stock_two_years_data(`update`, `num`, `stock_name`, `rise`) values("{0}", {1}, "{2}", {3})'.format(v[2], v[0], v[1], v[3])
        # print(sql)
        cur.execute(sql)
        count = count + 1
    print('数据库写入完毕,耗时：{:.4f}秒'.format(time.time() - start))
    conn.close()
    print('数据库链接关闭...成功')
except:
    print(sys.exc_info()[1])
    sys.exit(1)