import heapq
inf = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
table = [inf] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
   q = []
   heapq.heappush(q, (0, start))
   table[start] = 0
   while q:
        dist, now = heapq.heappop(q)
        if table[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < table[i[0]]:
                table[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0

max_distance = 0
for d in table:
    # 도달할 수 있는 노드인 경우
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
