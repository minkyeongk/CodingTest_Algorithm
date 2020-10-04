def is_bal(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:        # 가장 작은 균형 문자열
            return i

def is_right(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: # (가 없다면
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    idx = is_bal(p)
    u = p[:idx + 1]
    v = p[idx + 1:]

    if is_right(u):
        answer = u + solution(v)

    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer