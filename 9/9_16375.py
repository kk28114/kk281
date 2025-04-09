file = open('9_16375.txt')
cc = 0
for line in file:
    line = sorted([int(x) for x in line.split()])
    countone, counttwo = 0, 0
    for num in line:
        if line.count(num) == 1:
            countone += 1
        if line.count(num) == 2:
            counttwo += 1
    rule1 = (counttwo == 2 and countone == 2)
    rule2 = ((line[3] + line[2]) > (2 * (line[1] + line[0])))
    rule3 = (line[3] % line[0] != 0)
    if rule1 and rule2 and rule3:
        cc += 1
print(cc)
