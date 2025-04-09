def max_row(row):
    inds = [i for i in range(len(row)) if row[i] == 1]
    res = -1
    if len(inds) < 2:
        return -1
    for i in range(len(inds) - 1):
        res = max(res, inds[i + 1] - inds[i] - 1)
    return res

file = open('26.txt')
rect = [[0] * 100 for _ in range(100)]
Trect = [[0] * 100 for _ in range(100)]
for line in file:
    x, y = [int(elem) - 1 for elem in line.split()]
    rect[x][y] = 1
    Trect[y][x] = 1

res1, res2 = 0, 0
for row in rect:
    res1 = max(res1, max_row(row))
for row in Trect:
    res2 = max(res2, max_row(row))
print(res1, res2)
