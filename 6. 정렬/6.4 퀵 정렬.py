# 6.4 퀵 정렬

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def Qsort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    Qsort(arr, start, right - 1)
    Qsort(arr, right + 1, end)

Qsort(arr, 0, len(arr)-1)
print(arr)