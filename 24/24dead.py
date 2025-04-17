import re

def find_max_expression(s):
    matches = re.findall(r'(?:0|[1-9A-F][0-9A-F]*)(?:[+*](?:0|[1-9A-F][0-9A-F]*))*', s)
    return matches


file = open('24-314.txt')
s = file.readline()
valid_exprs = find_max_expression(s)
valid_exprs.sort(key= len, reverse=True)
print(valid_exprs[0])

res = valid_exprs[0]

operations = []
for x in res:
    if x in '+*':
        operations.append(x)
res_copy = res.replace('+', ' ').replace('*', ' ').split()
for i in range(len(res_copy)):
    res_copy[i] = int(res_copy[i], 16)

total_s = ''
for i in range(len(operations)):
    total_s += str(res_copy[i]) + operations[i]
total_s += str(res_copy[-1])

print(eval(total_s))
