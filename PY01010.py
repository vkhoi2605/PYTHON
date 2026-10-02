for t in range(int(input())):
    s = input()
    dau = s[:2]
    cuoi = s[-2:]
    if dau == cuoi:
        print("YES")
    else :
        print("NO")