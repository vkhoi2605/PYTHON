from itertools import product

nums = int(input())
products = {}
for _ in range(nums):
    product_name, price_str = input().split()
    products[product_name] = int(price_str)
orders = input().split()
counts = {}