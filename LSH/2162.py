# 문제
# N개의 선분들이 2차원 평면상에 주어져 있다. 선분은 양 끝점의 x, y 좌표로 표현이 된다.

# 두 선분이 서로 만나는 경우에, 두 선분은 같은 그룹에 속한다고 정의하며,
# 그룹의 크기는 그 그룹에 속한 선분의 개수로 정의한다. 두 선분이 만난다는 것은
# 선분의 끝점을 스치듯이 만나는 경우도 포함하는 것으로 한다.

# N개의 선분들이 주어졌을 때, 이 선분들은 총 몇 개의 그룹으로 되어 있을까?
# 또, 가장 크기가 큰 그룹에 속한 선분의 개수는 몇 개일까? 이 두 가지를 구하는 프로그램을 작성해 보자.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 3,000)이 주어진다. 
# 둘째 줄부터 N+1번째 줄에는 양 끝점의 좌표가 x1, y1, x2, y2의 순서로 주어진다. 각 좌표의 절댓값은 5,000을 넘지 않으며, 
# 입력되는 좌표 사이에는 빈칸이 하나 있다.

# 출력
# 첫째 줄에 그룹의 수를, 둘째 줄에 가장 크기가 큰 그룹에 속한 선분의 개수를 출력한다.

class line:
    def __init__(self, li) -> None:
        self.x1 = li[0]
        self.y1 = li[1]
        self.x2 = li[2]
        self.y2 = li[3]

    def change(self):
        self.x1, self.y1, self.x2, self.y2 = self.x2, self.y2, self.x1, self.y1
    
    def xy1(self):
        return [self.x1, self.y1]
    def xy2(self):
        return [self.x2, self.y2]

def ccw(pivot : line, x3, y3):
    return pivot.x1 * pivot.y2 + pivot.x2 * y3 + x3 * pivot.y1 - pivot.x2 * pivot.y1 - x3 * pivot.y2 - pivot.x1 * y3

def isCross(line1 : line, line2 : line):
    first = ccw(line1, line2.x1, line2.y1) * ccw(line1, line2.x2, line2.y2)
    second = ccw(line2, line1.x1, line1.y1) * ccw(line2, line1.x2, line1.y2)
    if first==0 and second==0:
        if line1.xy1() > line1.xy2():
            line1.change()
        if line2.xy1() > line2.xy2():
            line2.change()
        if line1.xy1() <= line2.xy2() and line2.xy1() <= line1.xy2():
            return True
        else:
            return False
    else:
        if first <= 0 and second <= 0:
            return True
        else:
            return False

def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]
    
def mergeline(a,b):
    q=find(a)
    w=find(b)
    if q==w:
        return
    else:
        if q<w:
            parent[w]=q
            cnt[q]+=cnt[w]
        else:
            parent[q]=w
            cnt[w]+=cnt[q]


linesLEN = int(input())
cnt=[1]*linesLEN
parent=[i for i in range(linesLEN)]
lines = []
prev = 0

for i in range(linesLEN):
    lines.append(line(list(map(int, input().split()))))


for i in range(linesLEN-1):
    for j in range(i+1,linesLEN):
        if isCross(lines[i], lines[j]):
            mergeline(i,j)

ans=[]
for i in range(linesLEN):
    ans.append(find(i))

print(len(set(ans)))
print(max(cnt))

