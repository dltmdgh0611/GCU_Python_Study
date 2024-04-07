nCnt = int(input())
numList = list(map(int, input().split()))
nCop = int(input())

matchCnt = 0

for i in range(0, nCnt):
    if numList[i] == nCop:
        matchCnt+=1
print(matchCnt)