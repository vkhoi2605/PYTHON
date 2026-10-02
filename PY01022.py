n = input()
sum = 0
cnt = 0
while len(n) > 1:
    sum = 0
    for i in n:
        sum += int(i)
    n = str(sum)
    cnt += 1
print(cnt)