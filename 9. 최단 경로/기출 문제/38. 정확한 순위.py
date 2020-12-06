# 38. 정확한 순위
# 모든 지점에서 다익스트라를 수행하되 순회 여부만 확인하는 느낌

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
table = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    table[a][b] = table[b][a] = 1

for i in range(1, n+1):
    for g in graph[i]:
        table[i][g] = 1
        table[g][i] = 1
        for x in graph[g]:
            if x not in graph[i] and table[i][x] == 0:
                graph[i].append(x)
        graph[i].remove(g)

cnt = 0
for i in range(1, n+1):
    if sum(table[i]) == n-1:
        cnt += 1
print(cnt)




