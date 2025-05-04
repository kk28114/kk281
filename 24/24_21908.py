file = open('24_21908.txt')
a = file.readline()
file.close()

alp = '0123456789ABCD'
even = '02468AC'
count, countm = 0, 0
for x in a:
    if x in alp:
        if x == '0' and count == 0:
            continue
        count += 1
        if x in even:
            countm = max(countm, count)
    else:
        count = 0
print(countm)
