# 특정 위치까지의 최대 개수에 더하기

n = int(input())
k = list(map(int, input().split()))
t = [k[0]] * n
t[1] = max(k[0], k[1])

for i in range(2, n):
    t[i] = max(t[i-2]+k[i], t[i-1])

print(t[n-1])
