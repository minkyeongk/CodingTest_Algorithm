# 7.6 떡볶이 떡 만들기
# 0부터 떡의 최대 길이까지가 범위

n, m = list(map(int, input().split(' ')))
dd = list(map(int, input().split()))

start = 0
end = max(dd)

result = 0
while start <= end:
    mid = (start + end)//2
    sum = 0

    for i in dd:
        if i > mid:
            sum += i-mid
    if sum < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result)
