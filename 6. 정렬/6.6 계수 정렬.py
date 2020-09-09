# 6.6 계수 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def counting_sort(arr):
    m = max(arr)+1
    cnt = [0] * m

    for n in arr:
        cnt[n] += 1
    for i in range(m):
        for j in range(cnt[i]):
            print(i, end=' ')

counting_sort(arr)
