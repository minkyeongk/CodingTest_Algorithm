# 25. 실패율

def solution(N, stages):
    answer = []
    num = []
    rate = []

    for i in range(N + 2):
        num.append(0)

    for j in stages:
        num[j] += 1

    for i in range(1, N + 1):
        s = sum(num[i:])
        if num[i] == 0 or s == 0:
            ratio = 0
        else:
            ratio = num[i] / s
        rate.append((i, ratio))

    rate = sorted(rate, key=lambda x: x[1], reverse=True)

    for i in rate:
        answer.append(i[0])

    return answer