# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，
# 然后再加上5天即本年的第几天，特殊情况，
# 闰年且输入月份大于2时需考虑多加一天：

year = int(input('年份:\n'))
month = int(input('月份:\n'))
day = int(input('天数:\n'))
summary = 0

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    summary = months[month - 1]
else:
    print("输入数据错误！")

summary += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    summary += 1
print('it is the %dth day.' % summary)

# 以上实例输出结果为：
# year:
# 2015
# month:
# 6
# day:
# 7
# it is the 158th day.
