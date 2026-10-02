for t in range(int(input())):
    s = input()
    check = True
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            check = False
    if not check:
        print('NO')
    else:
        print('YES')