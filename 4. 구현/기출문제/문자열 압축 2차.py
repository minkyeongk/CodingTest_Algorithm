# 2020 카카오 블채 - 문자열 압축
# 코드를 단순화하기위해 문자열 처리를 생략한 버전
# 코드는 간략해졌으나 정확도가 떨어짐

def solution(s):
    L = len(s)
    result = []     # 리스트를 굳이 만들 필요가 없었음
    for i in range(1, L // 2 + 1):
        prev, next = 0, i
        l = L       # 문자열을 복사하는 것이 아니라 문자열 길이를 복사, 빼나가는 방식으로 구현
        cnt, n = 0, 0           # cnt = 문자열에 들어가는 숫자 개수, n = 문자열 반복 횟수 (두개의 문자열이 반복되면 1)
        while next + i <= L:
            if s[prev:prev + i] == s[next:next + i]:
                print(prev, next)
                n += 1
            # 마지막 문자열이 위의 if문 처리 후에 cnt에도 반영되어야 하기 때문에 if문으로 구성
            if s[prev:prev + i] != s[next:next + i] or next + i == L:
                if n != 0:
                    print(n, i)
                    l = l - n * i
                    cnt += 1
                    n = 0
            prev = next
            next += i
        result.append(cnt + l)
    return min(result)
