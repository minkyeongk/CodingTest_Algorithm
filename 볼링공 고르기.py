n, m = map(int, input().split())
arr = list(map(int, input().split()))
weight = [0] * 11

for i in arr:
    weight[i] += 1
result = 0
for i in range(1, m + 1):
    n -= weight[i]
    result += weight[i] * n

print(result)
