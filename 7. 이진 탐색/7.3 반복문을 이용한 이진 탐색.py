# 7.3 반복문을 이용한 이진 탐색
# 셋다 겹치는 지점 기준으로 구현해도 되긴 하는데 효율이 떨어질 듯

def binary_search(start, end, find, arr):
    while start <= end:
        mid = (start + end) // 2
        if find == arr[mid]:
            return mid+1
        # start, end, mid가 모두 같아지는 지점에 답이 있을 수 있기 때문에
        # start와 end가 같은게 범위에 포함되지만, 답이 없을 경우 바로 반복문 탈출
        elif start == end:
            return None
        elif find > arr[mid]:
            start = mid+1
        else:
            end = mid-1

    return None

num = int(input("원소 개수를 입력하세요: "))
find = int(input("찾고자 하는 수를 입력하세요: "))

print("숫자 원소들을 띄어쓰기로 구분하여 입력하세요")
arr = list(map(int, input().split()))
arr.sort()
result = binary_search(0, num-1, find, arr)

if result == None:
    print("찾고자 하는 원소가 없습니다.")
else:
    print(result, "번째 원소입니다.")


# 이진 탐색 전체 복습 코드
# 재귀함수 ver
def binary_search1(arr, sch, start, end):
    mid = (start + end) // 2
    #print(mid)
    # 기존에 start와 end로 처리해줬을 때는 mid와 같은지 확인하고 확인해줌

    # or end < mid 이게 없어도 되네
    if start > mid:
        return -1

    if arr[mid] == sch:
        return mid

    elif arr[mid] > sch:
        return binary_search1(arr, sch, start, mid-1)

    else:
        return binary_search1(arr, sch, mid+1, end)

# 반복문 ver
def binary_search2(arr, sch, start, end):
    mid = (start + end) // 2
    while start <= mid:
        if arr[mid] == sch:
            return mid
        elif arr[mid] > sch:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return -1

arr = list(map(int, input().split()))
sch = int(input())

arr.sort()
print(arr)

result1 = binary_search1(arr, sch, 0, len(arr)-1)
if result1 == -1:
    print("not found")
else:
    print(result1)

result2 = binary_search2(arr, sch, 0, len(arr)-1)
if result2 == -1:
    print("not found")
else:
    print(result1)

# 원래는 start와 end로 처리
