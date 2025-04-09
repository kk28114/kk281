file = open('26yandex.txt')
a = file.readline()
dd = {}
for line in file:
    riad, mesto = [int(x) for x in line.split()]
    if riad not in dd:
        dd[riad] = []
        dd[riad].append(mesto)
    else:
        dd[riad].append(mesto)
dd = sorted(dd.items(), reverse= True)
print(dd)
for key, value in dd:
    value.sort()
    for i in range(1, len(value)):
        if value[i] - value[i - 1] >= 5:
            print(key,value[i - 1] + 3)
