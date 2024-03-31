a, b = map(int, input().split())

result = a-b

if result < 0:
    result = -result

print(result)