def tongCS(n):
    sum = 0
    for i in n:
        sum += (ord(i) - ord('0'))
    return sum

def check(n):
    if (tongCS(n) % 10 != 0):
        return False
    for i in range(len(n) - 1):
        if abs(ord(n[i]) - ord(n[i + 1])) != 2:
            return False
    return True

for t in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")