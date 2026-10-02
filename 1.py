a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))
d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1
dy = a1 * c2 - a2 * c1
if d == 0:
    if dx == 0:
        print("VSN")
    else:
        print("VN")
else:
    x = dx / d
    y = dy / d
    print(f"x = {x}, y = {y}")