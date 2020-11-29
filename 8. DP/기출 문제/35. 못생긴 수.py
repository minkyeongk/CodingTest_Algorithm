# 35. 못생긴 수
# 1부터 해서 다 해보면 되는거 아닌가

n = int(input())
cnt = 0
i = 1
while True:
    j = i       # 대신 확인 연산할 수 j에 i 대입
    while j % 2 == 0:
        j //= 2
    while j % 3 == 0:
        j //= 3
    while j % 5 == 0:
        j //= 5
    if j == 1:      # i가 못생긴 수인 경우
        cnt += 1
        if cnt == n:
            print(i)
            break
    i += 1

# 답안 코드 보며 최적화 해보기