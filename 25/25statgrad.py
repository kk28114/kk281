from math import sqrt
def dividers(n):
    div = set()
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

def isprime(n):
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True

def f(n):
    prime_div = [d for d in dividers(n) if isprime(d)]
    if len(prime_div) == 0:
        return 0
    return max(prime_div)

n = 1_750_000 + 1
count = 0
while count != 5:
    M = f(n)
    if M <= 15000 and M % 10 == 7:
        print(n)
        count += 1
    n += 1
