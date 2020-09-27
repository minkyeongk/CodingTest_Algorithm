dp = [0, 1, 1, 1, 0, 1] + [0] * 30000


def fun(n):
    if dp[n] != 0:
        return dp[n]
    m = 30000
    if n % 5 == 0:
        m = fun(n // 5) + 1
    if n % 3 == 0:
        m = min(m, fun(n // 3) + 1)
    if n % 2 == 0:
        m = min(m, fun(n // 2) + 1)
    m = min(m, fun(n - 1) + 1)
    return m


x = int(input())

print(fun(x))
