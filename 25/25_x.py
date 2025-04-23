def factor(n):
    res = []
    d = 2
    while d**2 <= n:
        if n % d == 0:
            res.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        res.append(n)
    return res

for n in range(800_000, 802_000 + 1):
    primes = set(factor(n))
    if len(primes) >= 2:
        p, s = 1, 0
        for num in primes:
            p *= num
            s += num
        if p % s == 0:
            print(n, p // s)
