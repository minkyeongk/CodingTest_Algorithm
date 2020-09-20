# 7.3 반복문을 이용한 이진 탐색
# 셋다 겹치는 지점 기준으로 구현해도 되긴 하는데 효율이 떨어질 듯

def binary_search(start, end, find, arr):
    while start <= end:
        mid = (start + end) // 2
        if find == arr[mid]:
            return mid+1
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