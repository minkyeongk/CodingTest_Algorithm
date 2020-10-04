
def possible(answer):
    for x, y, cons in answer:
        if cons == 0:  # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif cons == 1:    # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for f in build_frame:
        x, y, cons, op = f
        if op == 0:
            answer.remove([x, y, cons])
            if not possible(answer):
                answer.append([x, y, cons])
        if op == 1:
            answer.append([x, y, cons])
            if not possible(answer):
                answer.remove([x, y, cons])
    return sorted(answer)