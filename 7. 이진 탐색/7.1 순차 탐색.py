# 7.1 순차 탐색
# 입력 받은 문자열에 대한 순차 탐색

def sequential_search(num, find, arr):
    for i in range(num):
        if arr[i] == find:
            return i+1
    return -1

num = int(input("원소 개수를 입력하세요: "))
find = input("찾고자 하는 문자열을 입력하세요: ")

print("문자열 원소들을 띄어쓰기로 구분하여 입력하세요")
arr = input().split()

result = sequential_search(num, find, arr)

if result == -1:
    print("찾고자 하는 원소가 없습니다.")
else:
    print(result, "번째 원소입니다.")

