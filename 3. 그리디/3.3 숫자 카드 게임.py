# 실전 3.3 숫자 카드 게임
# 행의 개수 n, 열의 개수 m 입력
# 각 카드에 적힌 숫자 (행렬값) 주어짐
# 카드에 적힌 숫자 출력

# 아이디어: 행의 최솟값만 보면 될 듯, 각 행의 최솟값 중에 가장 큰거
#          행의 최솟값만 즉각적으로 구하기 때문에 굳이 행렬 모양대로 입력 받지 않아도 될 듯

n, m = map(int, input().split())
Max = 0

for i in range(n):
    List = list(map(int, input().split()))
    listMin = min(List)     # 이 행에서 가장 작은 값
    if listMin > Max: Max = listMin     # 위에서 구한 값과 지금까지 가장 큰 값을 비교

print(Max)
