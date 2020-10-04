n, u = map(int, input().split())
table = [i for i in range(n+1)]     # 맨 앞 제외

def find(table, nd):
    if table[nd] != nd:
        table[nd] = find(table, table[nd])
    return table[nd]

def union(a, b, table):     # b가 더 큰 수가 되도록
    r1 = find(table, a)
    r2 = find(table, b)
    if r1 > r2:
        table[a] = r2
    else:
        table[b] = r1

edge = []
result = 0

for _ in range(u):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()

for e in edge:
    cost, a, b = e
    if find(table, a) != find(table, b):
        union(a, b, table)
        result += cost

print(result)