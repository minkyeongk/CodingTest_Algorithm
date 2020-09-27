inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
table = [inf] * (n + 1)

for _ in range(m):
    f, t, d = map(int, input().split())
    graph[f].append((t, d))

def minimum():
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
    for j in graph[start]:
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