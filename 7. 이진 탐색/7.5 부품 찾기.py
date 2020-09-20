# 7.5 부품 찾기

n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

# 시간 복잡도 생각 안하고 푼 방법
for i in want:
    if i in have:
        print("yes", end=" ")
    else:
        print("no", end=" ")
print('\n')

# 계수 정렬 > 최악의 경우 20만번 연산,크기 100만의 리스트 생성
arr = ["no"]*1000000
for i in set(have):
    arr[i] = "yes"

for j in want:
    print(arr[j], end=" ")