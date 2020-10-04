n, m = map(int, input().split())
don = []    # 화폐 종류 담는 배열
for i in range(n):
    won = int(input())
    if won <= m:    # 화폐 크기가 가치의 합을 넘는지 확인
        don.append(won)

dp = [10000]*(m+1)
so = min(don)

for i in don:   # 화폐 종류에 해당하는 인덱스 1로 초기화
    dp[i] = 1

# 1만 더하면 안되지 않나?
for j in range(so*2, m+1):  # 화폐 종류 이외에 나올 수 있는 가장 작은 가격 so*2
    temp = []
    for k in don:       # j 금액에서 가능한 경우를 모두 temp에 저장, bottom-up 이긴 한데 접근 방식은 top-down
        temp.append(dp[j-k]+1)  # j-k가 가능하지 않은 가격이면 10000을 넘어가게 됨, 아래에서는 if로 걸러 받을 수 있는걸 여기서는 다 연산
    dp[j] = min(temp)

if dp[m] >= 10000:
    print(-1)
else:
    print(dp[m])

# 복습 코드
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

x = [0] + [m] * m

# 이중 포문, 최대 100만번 연산
for i in range(m):
    for j in arr:
        if i != m and i+j <= m:     # if로 안걸러줘도 문제는 없을 듯, 어차피 최솟값이 아닐거기 때문에
            x[i+j] = min(x[i+j], x[i]+1)    # 위에서 배열에 넣었다가 min 해준걸 이렇게 처리

print(x[m] if x[m] != m else -1)



