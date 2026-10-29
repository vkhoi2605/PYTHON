s = input()
print("NO" if s[0] == '8' or s.count("888") or s.count("6") + s.count("8") != len(s) else "YES")