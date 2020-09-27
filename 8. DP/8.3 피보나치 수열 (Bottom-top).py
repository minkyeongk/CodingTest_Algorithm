dp = [0, 1, 1] + [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibo(4))