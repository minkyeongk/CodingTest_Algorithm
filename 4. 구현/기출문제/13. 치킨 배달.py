# 시도중..
from itertools import permutations
from collections import deque

n, m = map(int, input().split())
city = []
home = []
chk = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chk.append([i, j])

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
jh = list(permutations(chk, m))
print(jh)

mnm = 1e9
for i in jh:        # 치킨집 조합
    sum = 0
    for j in home:  # 모든 집의 치킨 거리 구하기, j는 지금 집의 좌표
        print(j)
        r, c = j[0], j[1]
        q = deque()     # j로부터의 치킨 거리를 구하기 위한 큐
        dis = 1e9
        for k in range(4):
            q.append([r+row[k], c+col[k]])
        print(q)

        while q:    # 치킨거리 구하기 위한 BFS
            now = q.popleft()
            if 0 <= now[0] < n and 0 <= now[1] < n:
                if now in i:
                    #temp = abs(j[0]-now[0]) + abs(j[1]-now[1])
                    dis = abs(j[0]-now[0]) + abs(j[1]-now[1])       # BFS니까 바로 나오는거 아닌가
                    print(dis)
                    break
            for k in range(4):
                temp = [now[0]+row[k], now[1]+col[k]]
                if temp != j:
                    q.append(temp)
                j = now
        if dis == 1e9:
            print("error")
        sum += dis
    print("조합 하나 끝남", sum)
    mnm = min(mnm, sum)
print(mnm)











