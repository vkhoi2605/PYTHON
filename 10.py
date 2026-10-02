for _ in range(int(input())):
    h, w = map(int, input().split())
    mat = []
    for i in range (h):
        row = [int(num_str) for num_str in input().split()]
        mat.append(row)
    print(mat)