# 6.5 파이썬의 장점을 살린 퀵 정렬

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def Qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return Qsort(left) + [pivot] + Qsort(right)


print(Qsort(arr))