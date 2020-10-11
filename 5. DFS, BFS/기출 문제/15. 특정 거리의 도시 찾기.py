# 15. 특정 거리의 도시 찾기
# 한 지점에서 다른 지점들까지의 최단 거리 구하기, 단방향 > 다익스트라 알고리즘
# while문 최대 30만, 아래 for문 30만
import heapq

inf = 1e9
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
table = [inf for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

table[x] = 0
q = []
for i in graph[x]:
    table[i] = 1
    heapq.heappush(q, [1, i])

while q:
    mid = heapq.heappop(q)
    mid_idx = mid[1]
    for i in graph[mid_idx]:    # i가 mid와 연결된 노드
        if table[i] > table[mid_idx]:
            table[i] = min(table[i], table[mid_idx] + 1)
            heapq.heappush(q, [table[i], i])

flag = 0
for i in range(1, n+1):
    if table[i] == k:
        print(i)
        flag = 1
if flag == 0:
    print(-1)








