# 5.2 큐 구현 예제
# collection 모듈의 deque로 구현, 탐색 속도 빠른 자료구조

from collections import deque

Q = deque()

Q.append(5)
Q.append(2)
Q.append(3)
Q.append(7)
print('삭제:', Q.popleft())
Q.append(1)
Q.append(4)
print('삭제:', Q.popleft())

print('큐 현황: (front)', Q, '(tail)')
Q.reverse()
print('큐 뒤에서부터:', Q)
# deque은 출력하면 자료형이 같이 나오는구나
