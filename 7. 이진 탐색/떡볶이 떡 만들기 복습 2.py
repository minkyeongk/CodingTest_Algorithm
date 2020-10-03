n, m = map(int, input().split())
arr = list(map(int, input().split()))

def func(arr):
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
            return mid
        elif cnt > m:
            start = mid+1
        else:
            end = mid-1

    return mid-1 if cnt < m else mid


print(func(arr))
