for t in range(int(input())):
    cnt = 0
    n, x, m = [float(i) for i in input().split()]
    while n < m:
        n += (n * x / 100)
        cnt += 1
    print(cnt)