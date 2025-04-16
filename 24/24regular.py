import re
file = open('24-300.txt')
st = r"([1-9][0-9]*]|0)([+*]([1-9][0-9]*|0))*"
expr_re = re.compile(st)
dd = set()
z = file.read()
start = 0
maxlen = 0
while True:
    asd = expr_re.search(z, start)
    if asd == None: break
    #print(asd)
    dd.add(asd[0])
    start = asd.start() + 1
qq = []

parts = list(dd)
parts.sort(key = lambda x: -len(x))

countm = 0
for part in parts:
    if len(part) > countm:
        for i in range(len(parts)):
            for j in range(i + countm + 1, len(parts)):
                sub = part[i:j + 1]
                try:
                    if eval(sub) == 0:
                        if len(sub) > countm:
                            countm = len(sub)
                            print(countm, sub)
                except:
                    continue
