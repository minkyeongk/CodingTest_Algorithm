# 9.5 전보
# 방향 그래프, 시간이라는 가중치 존재
# 출발지점 한 곳, 최대한 많은 지점(가능한 모든 지점)으로 전송 > 다익스트라
# 도시의 개수: 전송 가능한 도시 개수, 걸리는 시간: 각 지점까지의 최소 경로 중 최대값

import heapq

inf = 1e9
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([z, y])
table = [1e9] * (n+1)
table[c] = 0

heap = []
heapq.heappush(heap, [0, c])    # 힙큐에 [출발지점으로부터의 거리, 인덱스] 넣어줌
while heap:
    mid = heapq.heappop(heap)
    mid_idx = mid[1]        # 0이 거리, 1이 인덱스

    for des in graph[mid_idx]:      # mid와 연결된 노드 des 체크
        des_idx = des[1]            # 헷갈리지 않도록 인덱스는 별도의 변수로 표기
        if table[des_idx] > table[mid_idx]:      # 1부터의 최소 거리가 더 크다 == 최단거리로 방문된 노드가 아니다
            table[des_idx] = min(table[des_idx], table[mid_idx] + des[0])     # des[0] mid와 des 간의 거리
            heapq.heappush(heap, [table[des_idx], des_idx])

cnt = 0
time = 0
for i in range(n+1):
    if table[i] != inf and i != c:
        cnt += 1
        time = max(time, table[i])

print(cnt, time)
