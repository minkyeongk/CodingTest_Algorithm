# 플로이드 워셜 복습 코드

n, e = map(int, input().split())
table = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    table[i][i] = 0

# 그래프를 테이블과 별개로 입력받을 필요가 없음
for _ in range(e):
    f, t, d = map(int, input().split())
    table[f][t] = d

# 원래 자신이 가지고 있던 값과 i번째 노드를 거쳐가는 값을 비교하여 값을 갱신
for i in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            table[start][end] = min(table[start][end], table[start][i] + table[i][end])

for i in range(1, n+1):
    print(table[i][1:])

