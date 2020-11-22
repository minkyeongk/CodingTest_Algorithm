# 34. 병사 배치하기
# 테스트 케이스들의 성공했는데 오답 나옴
# 7 - 9 8 7 4 11 6 5
# 8 - 9 8 11 10 7 4 5 2

n = int(input())
army = list(map(int, input().split()))

cnt = 0
before, next = 0, 1
while next < len(army):
    if army[before] <= army[next]:
        less = 0
        for x in army[next:]:
             less = less+1 if x >= army[before] else less
        big = 0
        for y in army[:next]:
            big = big+1 if y <= army[next] else big
        print(big, less)
        if big < less:
            cnt += big
            before = next
            next += 1
        else:
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




