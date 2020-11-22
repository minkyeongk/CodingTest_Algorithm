# 26. 카드 정렬하기
# 풀었던건데 다시 풀었네.. 매번 정렬해줘야 하니까 heap 쓰는 아이디어 

import heapq

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

result = 0
for _ in range(n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    temp = a+b
    result += temp
    heapq.heappush(arr, temp)

print(result)