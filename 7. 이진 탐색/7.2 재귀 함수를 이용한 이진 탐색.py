# 7.2 재귀함수를 이용한 이진 탐색
# 범위에 다시 mid를 포함할 필요가 없음

def binary_search(start, end, find, arr):
    mid = (start+end)//2
    if find == arr[mid]:
        return mid+1
    # start, end, mid가 모두 같아지는 지점에 답이 있을 수 있기 때문에
    # 찾고자 하는 원소인지 부터 확인하고 범위 체크
    elif start >= end:
        return None
    elif find < arr[mid]:
        return binary_search(start, mid-1, find, arr)
    else:
        return binary_search(mid+1, end, find, arr)

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





