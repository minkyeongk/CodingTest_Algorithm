import heapq

# 힙을 사용한 다익스트라 알고리즘
# 노드의 개수 n, 간선의 개수 e
# 그래프 graph, 출발점 start

n, e = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(e):
    # 세개 다 입력 받고 접근을 인덱스로 하기
    f, t, d = map(int, input().split())
    graph[f].append([t, d])

start = int(input())

# 최단거리 테이블 초기화
table = [1e9] * (n+1)
table[start] = 0
q = []
# 힙큐로 인해 갔다왔는지, 최소 거리의 노드가 무엇인지를 개별적으로 체크하지 않아도 됨
heapq.heappush(q, (0, start))   # 힙큐는 첫번째 원소를 기준으로 구성, 첫번째 원소를 거리로 지정
last = 0        # 노드를 처리한 적 있는지 확인하기 위한 변수

while len(q) != 0:
    #print(q)
    dis, nd = heapq.heappop(q)
    if dis < last:      # 저번에 처리한 노드의 거리보다 작다 > 이미 처리한 변수, 힙큐이기 때문에
        continue
    for i in graph[nd]:     # 연결된 모든 노드 순환, 0은 연결된 노드 번호, 1은 nd와의 거리
        table[i[0]] = min(table[i[0]], table[nd]+i[1])
        heapq.heappush(q, (table[i[0]], i[0]))
    last = dis

print(table[1:])


# 저번 코드
inf = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
table = [inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start = int(input())

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

for i in range(1, n + 1):
    if table[i] == inf:
        print("invalid route")
    else:
        print(table[i])