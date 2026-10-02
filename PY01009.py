s = input()
lower = 0
for i in s:
    if i.islower():
        lower += 1
if lower >= len(s) - lower:
    s = s.lower()
else :
    s = s.upper()
print(s)