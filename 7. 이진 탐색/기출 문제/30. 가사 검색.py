# 30. 가사 검색
# 효율성 테스트 1, 2, 3 통과 못함, 점수 55점

def find_right(q_word, start, end):
    mid = (start + end) // 2
    if q_word[mid] != '?' and q_word[mid + 1] == '?':
        return mid
    elif q_word[mid] == '?':
        return find_right(q_word, start, mid - 1)
    else:
        return find_right(q_word, mid + 1, end)


def find_left(q_word, start, end):
    mid = (start + end) // 2
    if q_word[mid] != '?' and q_word[mid - 1] == '?':
        return mid
    elif q_word[mid] == '?':
        return find_left(q_word, mid + 1, end)
    else:
        return find_left(q_word, start, mid - 1)


def solution(words, queries):
    answer = [0] * len(queries)

    by_len = dict()
    for w in words:
        l = len(w)
        if l in by_len:
            by_len[l].append(w)
        else:
            by_len[l] = [w]

    # 인덱스로 접근하기
    for i in range(len(queries)):
        q = queries[i]
        q_len = len(q)
        if q_len in by_len:
            for word in by_len[q_len]:
                if q[0] != '?':  # 앞에서부터 시작
                    right = find_right(q, 0, q_len)
                    if q[:right + 1] == word[:right + 1]:
                        answer[i] += 1
                else:
                    left = find_left(q, 0, q_len)
                    if q[left:] == word[left:]:
                        answer[i] += 1
    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                  ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)