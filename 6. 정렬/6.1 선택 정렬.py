# 6.1 선택 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        idx = arr.index(min(arr[i:]))
        arr[i], arr[idx] = arr[idx], arr[i]

selection_sort(arr)
print(arr)