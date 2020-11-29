# 29. 공유기 설치

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

# 최소 거리 임의로 설정
start = arr[1] - arr[0]
# 최대 거리
end = arr[-1] - arr[0]

result = 0
while (start <= end):
    mid = (start + end) // 2  # 최적 거리 구하기 위한 초기값
    old = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= old + mid:  # mid가 최적 결과라는 가정하에 공유기 설치
            count += 1
            old = arr[i]

    # 남은 공유기 개수에 따라 간격 조정
    if count >= c:      # 더 설치할 수 있는 경우: 간격 넓힘
        start = mid + 1
        result = mid
    else:
        end = mid - 1   # 개수 다 채우지 못한 경우: 간격 좁힘

print(result)


