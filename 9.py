for _ in range(int(input())):
#    a, b = map(int, input().split())
    a, b = [int(num_str) for num_str in input().split()]
    while b != 0:
        a, b = b, a % b
    print(a)