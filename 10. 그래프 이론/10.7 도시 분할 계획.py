def find(table, x):
    if table[x] != x:
        table[x] = find(table, table[x])
    return table[x]

def union(table, a, b):
    a = find(table, a)
    b = find(table, b)
    if a < b:
        table[b] = a
    else:
        table[a] = b

n, m = map(int, input().split())
table = [0] * (n + 1)

e = []
result = 0

for i in range(1, n+1):
    table[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    e.append((cost, a, b))

e.sort()
last = 0

for edge in e:
    cost, a, b = edge
    if find(table, a) != find(table, b):
        union(table, a, b)
        result += cost
        last = cost

print(result - last)
