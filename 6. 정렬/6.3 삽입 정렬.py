# 6.3 삽입 정렬
# 한번에 밀어넣는 것이 아니라 한칸씩 확인하는 것
# 어디서 부터 확인하는지 정확히 확인하기

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

insertion_sort(arr)
print(arr)
