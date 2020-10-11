# 17. 경쟁적 전염

import heapq

n, k = map(int, input().split())
m = []
ord = []
for i in range(n):
    m.append(list(map(int, input().split())))
    for j in range(n):
        if m[i][j] != 0:
            heapq.heappush(ord, [m[i][j], i, j])    # 종류, 행, 렬
s, x, y = map(int, input().split())

bh = [[0, -1], [0, 1], [-1, 0], [1, 0]] #  상하좌우
for i in range(s):
    l = len(ord)
    other = []
    for _ in range(l):
        now = heapq.heappop(ord)
        for z in bh:
            row = now[1]+z[0]
            col = now[2]+z[1]
            if 0 <= row < n and 0 <= col < n:
                if m[row][col] == 0:
                    m[row][col] = now[0]
                    heapq.heappush(other, [now[0], row, col])
    ord = other     # 같은 힙에 넣어버리면 종류를 한번 다 돌기 전에 새로 들어온 이전의 종류로 넘어가버림

print(m[x-1][y-1])
