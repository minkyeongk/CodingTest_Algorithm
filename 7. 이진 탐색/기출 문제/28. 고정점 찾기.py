# 28. 고정점 찾기
# 다시 풀어보기!

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, 0, mid-1)
    else:
        return binary_search(arr, mid+1, end)


n = int(input())
arr = list(map(int, input().split()))
result = binary_search(arr, 0, len(arr)-1)

print(result if result is not None else -1)