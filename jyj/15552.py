import sys

n = int(sys.stdin.readline().rstrip())
for i in range(0, n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)