# 37. 플로이드
# python3으로는 시간 초과 나옴, pypy3는 가능

n = int(input())
m = int(input())
table = [[1e9] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())     # 방향 그래프
    table[a][b] = min(table[a][b], c)   # 이걸 if문으로 바꾸면 시간초과가 안뜰까?
for i in range(1, n+1):
    table[i][i] = 0

for x in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            table[i][j] = min(table[i][j], table[i][x]+table[x][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        chk = table[i][j] if table[i][j] != 1e9 else 0
        print(chk, end=' ')     # end 처리 까먹으면 안됨
    print()     # 여기서 줄바꿈 출력해주면 불바꿈 두번 된다, print가 기본적으로 줄바꿈을 지원하기 때문
