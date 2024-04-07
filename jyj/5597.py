numList = []

for i in range(0,28):
    chulsuk = int(input())
    numList.append(chulsuk)

for i in range(1,31):
    if i not in numList:
        print(i)