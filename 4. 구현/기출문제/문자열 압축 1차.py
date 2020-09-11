# 2020 카카오 블채 - 문자열 압축
# 문제 그대로 구현으로 옮기고자 한 버전
# 문자열을 카피하여 문제 설명을 그대로 구현하고자 함

def solution(S):
    S = list(S)
    L = len(S)

    result = []
    for i in range(1, L // 2 + 1):
        s = S.copy()
        pre, ne = 0, i      # pre -> prev, ne ->next
        n = 1
        while ne + i <= len(s):
            if s[pre:pre + i] == s[ne:ne + i]:
                if n == 1:      # 해당 문자열에 대한 중복이 처음 일어난 경우
                    for _ in range(i):
                        s.pop(pre)
                    n += 1
                    s.insert(pre, n)
                    pre += 1
                    ne = pre + i
                else:           # 중복이 처음이 아닌 경우
                    s[pre - 1] += 1
                    n += 1
                    for _ in range(i):
                        s.pop(pre)
            else:
                n = 1
                pre += i
                ne += i
        result.append(len(s))
    return min(result)
