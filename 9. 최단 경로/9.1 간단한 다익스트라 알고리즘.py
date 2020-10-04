# 기본 다익스트라 알고리즘 복습

# 그래프 입력
# 노드의 개수와 간선의 개수 입력
n, e = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(e):
    # 세개 다 입력 받고 접근을 인덱스로 하기
    f, t, d = map(int, input().split())
    graph[f].append([t, d])

start = int(input())
visited = [1] + [0] * n

# 최단거리 테이블 초기화
table = [1e9] * (n+1)
table[start] = 0
nd = start

while True:
    #print(nd)
    visited[nd] = 1
    for i in graph[nd]:     # 연결된 모든 노드 순환
        if visited[i[0]] == 0:
            table[i[0]] = min(table[i[0]], table[nd]+i[1])

    # 아래의 minimum 함수에 해당하는 부분 + 종료 조건 (연결된 노드를 다 돌았을 때)
    temp = [j for j in range(n+1) if visited[j] == 0 and table[j] != 1e9]
    if len(temp) == 0:      # visited하지 않은 노드가 없는 경우
        break

    nd = temp[0]
    for k in temp:
        nd = k if table[k] < nd else nd

print(table[1:])

# 저번 코드 > 연결되지 않은 노드가 있는 경우에도 1e9로 연산이 들어가겠지
inf = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
table = [inf] * (n + 1)

for _ in range(m):
    f, t, d = map(int, input().split())
    graph[f].append((t, d))
start = int(input())

def minimum():      # 최단 거리 노드를 구해주는 함수
    min_value = inf
    index = 0
    for i in range(1, n + 1):
        if table[i] < min_value and not visited[i]:
            min_value = table[i]
            index = i
    return index

def dijkstra(start):
    table[start] = 0
    visited[start] = True
    for j in graph[start]:      # 첫 노드와 연결된 노드 테이블 초기화
        table[j[0]] = j[1]

    for i in range(n - 1):
        now = minimum()
        visited[now] = True

        for j in graph[now]:
            table[j[0]] = min(table[now] + j[1], table[j[0]])

dijkstra(start)

for i in range(1, n + 1):
    if table[i] == inf:
        print("invalid route")
    else:
        print(table[i])