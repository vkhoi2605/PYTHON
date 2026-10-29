n = input()
tmp = len(n) % 3
if tmp != 0:
    for i in range(tmp, 3):
     n = '0' + n
ans = ''
for i in range(len(n) - 1, -1, -3):
    s = ((int(n[i - 1]) * 2) ** 1 + (int(n[i - 2]) * 2) ** 2)
    if int(n[i]) == 0:
       ans += str(s)
    else :
       ans += str(s + 1)
print(ans[::-1])