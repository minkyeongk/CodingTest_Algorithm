# 5.1 스택 구현 예제
# 파이썬의 리스트 사용하여 구현

stk = []

stk.append(5)   # append가 push 함수
stk.append(2)
stk.append(3)
stk.append(7)
print('삭제:', stk.pop())
stk.append(1)
stk.append(4)
print('삭제:', stk.pop())

print('스택 현황:', stk, '(top)')
print('스택 거꾸로: (top)', stk[::-1])
