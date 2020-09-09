# 6.6 두 배열의 원소 교체

# 정렬을 사용하지 않은 방법
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    ai = a.index(min(a))
    bi = b.index(max(b))
    if a[ai] >= b[bi]: break
    a[ai], b[bi] = b[bi], a[ai]

print(sum(a))

# 정렬을 사용하여 시간 복잡도 최적화 하는 방법
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
l = len(b)-1

for i in range(k):
    if a[i] >= b[l-i]:
        break
    a[i], b[l-i] = b[l-i], a[i]

print(sum(a))
