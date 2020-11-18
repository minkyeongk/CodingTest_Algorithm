# 31. 금광
# 전형적인 DP, 최소 문제를 어디서 뽑아내야할지 생각하기

t = int(input())
for k in range(t):
    n, m = map(int, input().split())
    arr = [[] for i in range(n)]

    temp = list(map(int, input().split()))
    idx = 0
    for i in range(n):
        for j in range(m):
            arr[i].append(temp[idx])
            idx += 1

    # 오른쪽에서부터 쌓아가야 함, 이전 단계에서 답을 도출함으로써 다음 단계에는 영향을 주지 않도록

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                top = 0
            else:
                top = arr[i-1][j-1]

            mid = arr[i][j-1]

            if i == n-1:
                bottom = 0
            else:
                bottom = arr[i+1][j-1]

            arr[i][j] += max(top, mid, bottom)

    result = 0
    for i in range(n):
        result = max(result, arr[i][m-1])
    print(result)






