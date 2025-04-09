from random import *
def solution_alex(a):
    a = '***' + a
    dp = [0] * len(a)
    for i in range(3, len(a)):
        if a[i] == 'Y' and a[i - 2] in 'XZ':
            dp[i] = dp[i - 3] + 1
    return max(dp)
def solution_roma(a):
    cc1, cc2, cc3 = 0, 0, 0
    ccmax = 0
    for x in range(2, len(a), 3):
        if (a[x - 2] == 'X' or a[x - 2] == 'Z') and a[x] == 'Y':
            cc1 += 1
            ccmax = max(ccmax, cc1)
        else:
            cc1 = 0

    for y in range(3, len(a), 3):
        if (a[y - 2] == 'X' or a[y - 2] == 'Z') and a[y] == 'Y':
            cc2 += 1
            ccmax = max(ccmax, cc2)
        else:
            cc2 = 0

    for z in range(4, len(a), 3):
        if (a[z - 2] == 'X' or a[z - 2] == 'Z') and a[z] == 'Y':
            cc3 += 1
            ccmax = max(ccmax, cc3)
        else:
            cc3 = 0
    return ccmax

for test in range(100):
    a = ''.join([choice('XYZ') for _ in range(randint(3, 200))])
    assert solution_roma(a) == solution_alex(a), f'{a}, {solution_roma(a)}, {solution_alex(a)}'
