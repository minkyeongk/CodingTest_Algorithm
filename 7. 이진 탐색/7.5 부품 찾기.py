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

# 복습 코드
# 계수 정렬
# 정렬해서 이진탐색 쓰면 정렬하는데 시간이 걸리니까
# 여러개가 나온다면? 중복되어 나온 경우는 개수를 더해주어야 하나?

n = int(input())
ok = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

stk = [0] * (max(ok) + 1)
for i in ok:
    stk[i] = 1
# 두 개 합치는 방법
# for i in input().split():
#   stk[int(i)] = 1

for j in chk:
    if stk[j] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")