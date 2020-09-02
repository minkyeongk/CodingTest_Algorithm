# 5.10 음료수 얼려먹기
# 행렬 헷갈리면 문제 조건 그대로 맞춰서 풀기

n, m = map(int, input().split())
ice = []

for k in range(n):
    ice.append(list(map(int, input())))


def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0

    if ice[i][j] == 1:
        return 0

    ice[i][j] = 1

    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)

    return 1


cnt = 0
for h in range(n):
    for w in range(m):
        cnt += dfs(h, w)

print(cnt)



