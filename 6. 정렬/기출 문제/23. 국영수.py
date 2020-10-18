# 23. 국영수
# sorted, key = lambda 함수 사용

student = []
n = int(input())
for _ in range(n):
    student.append(input().split())     # 대괄호 없어도 리스트로 들어가지는구나

result = sorted(student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in result:
    print(i[0])
