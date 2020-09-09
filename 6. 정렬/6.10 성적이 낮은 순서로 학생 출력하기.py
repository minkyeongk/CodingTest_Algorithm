# 6.10 성적이 낮은 순서로 학생 출력하기

n = int(input())
arr = []

for i in range(n):
    st = input().split()
    arr.append((st[0], int(st[1])))

arr = sorted(arr, key=lambda x: x[1])
for n in arr:
    print(n[0], end=' ')

