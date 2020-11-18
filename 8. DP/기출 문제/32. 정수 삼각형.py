# 32. 정수 삼각형
# 입력 형태만 다를 뿐 금광과 완전히 동일한 문제

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 긱 층마다 idx-1 : 좌상향, idx: 우상향
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            left = 0
        else:
            left = arr[i-1][j-1]
        if j == i:
            right = 0
        else:
            right = arr[i-1][j]
        arr[i][j] += max(left, right)

print(max(arr[n-1]))

