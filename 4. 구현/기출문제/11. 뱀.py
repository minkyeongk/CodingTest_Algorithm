# 11. 뱀
# 매초마다 이동, 방향 변환은 매초마다 하진 않음
# 어떤 자료형과 어떤 구조, 어떤 알고리즘을 사용해야할지 생각하고 문제 풀기
# 문제 똑바로 읽기 : x초가 끝난 뒤에 방향 변환
# 테이블 상으로만 뱀을 표시하려고 하였으나 tail 처리에 문제 발생
# > 뱀을 개별적인 리스트로 처리
# 숫자 범위 자체가 작기 때문에 시간 생각하지 않아도 될 듯

n = int(input())
table = [[0 for _ in range(n+1)] for _ in range(n+1)]
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    table[i][j] = 1

X = []
C = []
l = int(input())
for _ in range(l):
    x, c = input().split()  # x만 형변환 해주기
    X.append(int(x))
    C.append(c)

# 동 남 서 북, 오른쪽 회전 인덱스 +1, 왼쪽 회전 인덱스 -1
# 행렬 헷갈리지 말기! 세로 가로임
col = [1, 0, -1, 0]
row = [0, 1, 0, -1]

bam = [[1, 1]]
bh = 0
time = 0
while True:
    time += 1           # 시간 이동
    if time-1 in X:       # 방향 변환, x초 이후에 방향 변환이기 때문에 > 체크와 방향변환을 아예 뒤로 빼주는게 나았을 수도
        idx = X.index(time-1)
        if C[idx] == 'L':
            bh = bh-1 if 0 <= bh-1 else 3
        else:
            bh = bh+1 if bh+1 < 4 else 0

    now = [bam[-1][0] + row[bh], bam[-1][1] + col[bh]]

    #  더 이상 갈 수 없는 경우
    if now[0] > n or now[0] < 1 or now[1] > n or now[1] < 1:
        break
    if now in bam:
        break

    # 사과가 있다면
    if table[now[0]][now[1]] == 1:
        table[now[0]][now[1]] = 0
        bam.append(now)
    # 사과가 없다면
    else:
        bam.pop(0)
        bam.append(now)

print(time)