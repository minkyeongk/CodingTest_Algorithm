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

for i in range(0, n + 1):
    table[i] = i

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(table, a, b)
    elif op == 1:
        if find(table, a) == find(table, b):
            print('YES')
        else:
            print('NO')
