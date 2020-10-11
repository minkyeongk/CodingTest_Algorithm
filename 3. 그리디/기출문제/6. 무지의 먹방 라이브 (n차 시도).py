# 2019 카카오 블채 - 무지의 먹방 라이브 (food_times -> food)
# k를 최적화까지는 아니더라도 대략적으로 줄이고자 함 (food_times를 돌 수 있는 최소 바퀴 수 m을 통해)
# 하지만 실패, 정확성과 효율성 모두 떨어짐
# 힙을 사용해서 최적화 시켜보자

def solution(food, k):
    if sum(food) <= k:
        return -1

    L = len(food)
    m = k // L      # k번이 food를 돌 수 있는 최소 횟수 라고 생각

    # 최소 횟수에 따른 food 처리 (m바퀴를 이미 돌았다 가정)
    for i in range(L):
        if food[i] <= m:
            k -= food[i]
            food[i] = 0
        else:
            k -= m
            food[i] -= m

    j = 0       # j가 먹어야할 인덱스, 즉 답
    while k >= 0:       # k번 돈다
        if food[j] > 0:
            k -= 1
        j += 1
        j %= L

    if sum(food) <= 0:      # 다 돌았는데 다 먹었을 경우
        return -1

    return j