file = open('24.txt')
a = file.readline()
file.close()

next = {
    'S': 'Q',
    'Q': 'R',
    'R': 'P',
    'P': 'S'
}

count, countm = 1, 1
for i in range(len(a) - 1):
    if next[a[i]] == a[i + 1]:
        count += 1
        countm = max(count, countm)
    else:
        count = 1
print(countm)
