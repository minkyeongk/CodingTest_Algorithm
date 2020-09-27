n, m = map(int, input().split())
don = []
for i in range(n):
    won = int(input())
    if won <= m:
        don.append(won)

dp = [10000]*(m+1)
so = min(don)

for i in don:
    dp[i] = 1

for j in range(so*2, m+1):
    temp = []
    for k in don:
        temp.append(dp[j-k]+1)
    dp[j] = min(temp)

if dp[m] >= 10000:
    print(-1)
else:
    print(dp[m])




