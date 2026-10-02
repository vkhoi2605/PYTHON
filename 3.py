fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
for i in range(len(fruits)):
    print(fruits[i])
for index, fruit in enumerate(fruits):
    print(index, fruit)
for stt, fruit in enumerate(fruits, start = 1):
    print(stt, fruit)