# 실전 4.3 왕실의 나이트

# 입력 현재 나이트의 좌표
# 출력 나이트가 이동할 수 있는 경우의 수

pos = input()
posx = ord(pos[0])
posy = int(pos[1])

l = [(2, 0), (-2, 0)]       # y에 1, -1
v = [(0, 2), (0, -2)]
cnt = 0

a = ord('a')
h = ord('h')

for n in l:
    x = posx + n[0]
    y = posy + 1
    y2 = posy - 1

    if a <= x <= h and 1 <= y <= 8:
        cnt += 1

    if a <= x <= h and 1 <= y2 <= 8:
        cnt += 1

for n in v:
    x = posx + 1
    x2 = posx - 1
    y = posy + n[1]

    if a <= x <= h and 1 <= y <= 8:
        cnt += 1

    if a <= x2 <= h and 1 <= y <= 8:
        cnt += 1

print(cnt)
