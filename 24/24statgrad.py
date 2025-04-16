file = open('24.txt')
a = file.readline()
file.close()

for digit in '12345':
    a = a.replace(digit, 'D')

a = a.replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ')
a = a.replace('--', ' ').replace('-*', ' ').replace('*-', ' ').replace('**', ' ')
parts = a.split()
parts.sort(key = lambda x: -len(x))

countm = 0
for part in parts:
    if len(part) > countm:
        for i in range(len(parts)):
            for j in range(i + countm + 1, len(parts)):
                sub = part[i:j + 1].strip('-')
                if '-00' not in sub and '-0D' not in sub and sub[:2] not in '00D' and sub.rfind('*') < sub.find('-'):
                    if len(sub) > countm:
                        countm = len(sub)
                        print(countm, sub)
