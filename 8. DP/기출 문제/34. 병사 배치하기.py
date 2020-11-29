# 34. 병사 배치하기
# 테스트 케이스들의 성공했는데 오답 나옴
# 7 - 9 8 7 4 11 6 5 : 3
# 8 - 9 8 11 10 7 4 5 2 :

n = int(input())
army = list(map(int, input().split()))

cnt = 0
before, next = 0, 1  # 앞, 뒤 인덱스
while next < len(army):
    if army[before] <= army[next]:
        # before을 고르는 경우
        less = 0    # 빠지는 인원 수
        should_big = army[before]
        for x in army[next:]:
            if should_big <= x:
                less += 1
            else:
                should_big = x
        # next를 고르는 경우 (앞은 이미 정렬되어 있기 때문에)
        big = 0     # 빠지는 인원 수
        for y in army[:next]:
            big = big + 1 if y <= army[next] else big
        #print(big, less)

        if big < less:  # next를 고르면
            cnt += big
            before = next
            next += 1
        else:       # before을 고르면
            cnt += less
            i = next
            while i < len(army):
                if army[i] >= army[before]:
                    army.pop(i)
                else:
                    i += 1
    else:
        before += 1
        next += 1
print(cnt)
