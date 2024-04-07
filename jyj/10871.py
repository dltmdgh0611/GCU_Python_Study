numCnt = list(map(int, input().split()))
numList = list(map(int, input().split()))

for i in range(0, numCnt[0]):
    if numList[i] < numCnt[1]:
        print(numList[i], end=" ")