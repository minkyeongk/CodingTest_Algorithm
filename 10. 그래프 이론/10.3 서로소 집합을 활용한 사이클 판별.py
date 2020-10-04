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

cycle = False

for i in range(u):
    a, b = map(int, input().split())
    if find(table, a) == find(table, b):
        cycle = True
        break
    else:
        union(a, b, table)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")