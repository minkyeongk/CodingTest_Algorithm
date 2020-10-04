n, u = map(int, input().split())
table = [i for i in range(n+1)]     # 맨 앞 제외
print(table)

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

for _ in range(u):
    a, b = map(int, input().split())
    union(a, b, table)

print([i for i in range(1, n+1)])
print(table[1:])