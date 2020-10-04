# 포함되는거
from itertools import permutations

def solution(n, weak, dist):
    l = len(weak)
    for i in range(l):
        weak.append(weak[i] + n)

    answer = len(dist)
    for start in range(l):
        for f in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[start] + f[cnt - 1]

            for idx in range(start, start + l):
                if pos < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + f[cnt - 1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer