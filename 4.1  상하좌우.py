# 예제 4.1 상하좌우
# 시작 좌표 (1, 1)
# 입력 공간의 크기 N

# 동 북 서 남
dy = [1, 0, -1, 0]      # 동, 서는 열이 바뀜
dx = [0, -1, 0, 1]      # 남, 북은 행이 바뀜
l = ['R', 'U', 'L', 'D']

x, y = 1, 1

n = int(input())
a = list(map(str, input().split()))

for i in a:
    j = l.index(i)
    x2 = x + dx[j]
    y2 = y + dy[j]

    if x2<1 or x2>n or y2<1 or y2>n:    # 공간 밖 무시
        continue

    x, y = x2, y2

print(x, y)


