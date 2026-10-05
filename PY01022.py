n = input()
cnt = 0
if len(n) == 1:
    cnt = 1
while len(n) > 1:
    s = 0
    for i in n:
        s += (ord(i) - ord('0'))
    n = str(s)
    cnt += 1
print(cnt)