n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start < end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += (i - mid) if i > mid else 0
        print(i, mid, cnt)
    print('\n')

    if cnt == m:
        result = mid
    # cnt가 더 작아져야 할 때, 더 잘라야 할 때
    elif cnt > m:
        result = mid
        start = mid+1
    else:
        end = mid-1

# 그냥 마지막까지 이진탐색으로 돌리고 cnt가 더 작은 경우 start-1을 반환한다면?

print(result)

