def f(s, p):
    '''
    :param s: строка
    :param p: макс. кол-во точек
    :return: макс. подстроку с условием на точки
    '''
    countm = 0
    points = 0
    l = 0
    for r in range(len(s)):
        if s[r] == '.':
            points += 1
        if points <= p:
            countm = max(countm, r - l + 1)
        else:
            while s[l] != '.':
                l += 1
            l += 1
            points -= 1
    return countm
file = open('24-181.txt')
parts = file.readline().split('Y')
countm = 0
for s in parts:
    countm = max(countm, f(s, 5))
print(countm)