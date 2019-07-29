# 题目：暂停一秒输出，并格式化当前时间。

# 程序源代码
# ======================================================
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# ======================================================

# 输出结果:
# 2019-07-29 18:54:40
# 2019-07-29 18:54:41
