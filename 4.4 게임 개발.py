# 실전 4.4 게임 개발
# 입력: n, m (행, 렬)
#      x, y, d (현재 좌표 (x, y), 현재 방향 d)
#      맵 정보

n, m = map(int, input().split())
nowX, nowY, nowD = map(int, input().split())

#     북 동 남 서
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
dr = [0, 1, 2, 3]

cnt = 0
table = []

for i in range(n):
    table.append(list(map(int, input().split())))
    for j in range(m):
        table[i][j] = [table[i][j], 0]

print(table)

spin = 0
while True:
    if spin == 4:
        spin = 0
        mv_idx = dr.index(nowD) - 2
        mvX, mvY = nowX + dx[mv_idx], nowY + dx[mv_idx]

        if table[mvX][mvY][0] == 1:
            break
        else:
            nowX = mvX
            nowY = mvY
            cnt += 1
            continue

    mv_idx = dr.index(nowD) - 1
    mvX, mvY = nowX + dx[mv_idx], nowY + dx[mv_idx]
    nowD = dr[mv_idx]

    if table[mvX][mvY][0] == 0 and table[mvX][mvY][1] == 0:
        nowX = mvX
        nowY = mvY
        cnt += 1
        table[mvX][mvY][1] = 1
    else:
        spin += 1       # 헛돌기

print(cnt)
