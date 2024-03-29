# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# 程序分析：
# 对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n < k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

# 程序源代码
# ======================================================


# end=''是python3中输出不换行的一种设置
def reduce_num(n):

    print('{:3d} = '.format(n), end='')

    # 判断输入是否是大于0的整数
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        # exit(0)：无错误退出
        # exit(1)：有错误退出
        # 退出代码是告诉解释器的（或操作系统）
        exit(0)
    # 如果是1，那么直接输出
    elif n == 1:
        print('{:2d}'.format(n))

    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于 n/index
                if n == 1:
                    print('{:2d}'.format(index))
                else:  # index 一定是素数
                    print('{:2d} *'.format(index), end='')
                break


reduce_num(90)
reduce_num(100)
# ======================================================

# 输出结果:
# 90 =  2 * 3 * 3 * 5
# 100 =  2 * 2 * 5 * 5
