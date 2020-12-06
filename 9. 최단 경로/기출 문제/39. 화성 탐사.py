# 39. 화성 탐사
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    #print(arr)

    for i in range(1, n):
        arr[i][0] += arr[i-1][0]
        arr[0][i] += arr[0][i-1]
    #print(arr)

    for i in range(1, n):
        for j in range(1, n):
            arr[i][j] += min(arr[i-1][j], arr[i][j-1])
            #print(i, j, arr[i][j])

    print(arr[n-1][n-1])