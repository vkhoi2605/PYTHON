for t in range(int(input())):
    s = input()
    letters = []
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else :
            letters.append(i)
    letters.sort()
    print(''.join(letters) + str(sum))