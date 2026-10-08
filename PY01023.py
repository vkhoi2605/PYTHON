from math import *

for t in range(int(input())):
    n = int(input())
    print("1", end = "")
    for i in range(2, int(sqrt(n + 1))):
        cnt = 0
        check = False
        while n % i == 0:
            cnt += 1
            n //= i
            check = True
        if check:
            print(" * " + str(i) + "^" + str(cnt), end = "")
    if n > 1:
        print(" * " + str(n) + "^1", end = "")
    print()
