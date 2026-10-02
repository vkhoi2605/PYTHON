t = int(input())
for i in range(t):
    n = int(input())
    p = 10
    while n > p:
        r = n % p
        n //= p
        if r * 2 >= p:
            n += 1
        n *= p
        p *= 10
    print(n)