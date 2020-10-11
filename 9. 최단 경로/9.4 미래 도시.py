# 9.4 미래 도시
# 출발지와 목적지가 다른 여러 최소 경로를 구해야 함
# 플로이드 워셜 알고리즘 사용
# 시간 복잡도 최대 백만

n, m = map(int, input().split())
table = [[101 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    table[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    table[a][b] = 1     # 무방향으로 거리 동일하기 때문
    table[b][a] = 1

x, k = map(int, input().split())

for mid in range(1, n+1):
    for st in range(1, n+1):
        for en in range(1, n+1):
            table[st][en] = min(table[st][en], table[st][mid]+table[mid][en])

result = table[1][k]+table[k][x]
if result < 101:
    print(result)
else:
    print(-1)

