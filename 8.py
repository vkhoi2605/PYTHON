t = int(input())
for i in range(t):
    n = int(input())
    rev_num = 0
    while n > 0:
        rev_num = rev_num * 10 + n % 10
        n //= 10
    print(rev_num)