# 29. 공유기 설치
# 이진 탐색하는 대상이 좌표가 아닌 거리

n, c = map(int, input().split())    # n: 집, c: 공유기
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()

start_dis = home[1] - home[0]
end_dis = home[-1] - home[0]
result = 0  # 가능한 최대의 값이니까 가능한 가장 작은 값으로 초기화

# 이진 탐색: 범위를 반으로 줄여나가면서 찾음, log n의 시간 복잡도
# 이진 탐색이 성립하는 (아주 기본) 조건: start가 end보다 작거나 같아야 (같을 때 답이 나올 수도 있기 때문에)
while start_dis <= end_dis:
    spot = home[0]    # 공유기 설치 위치, 첫 좌표에는 무조건 설치한다고 가정
    cnt = 1     # 설치된 공유기의 개수
    mid_dis = (start_dis+end_dis) // 2      # 현재 start와 end 가 만든 mid
    for i in range(len(home)):  # 현재 mid로 공유기 설치해봤을 때, i는 인덱스
        if spot+mid_dis <= home[i]:    # 현재 위치에서 mid를 더한 것보다 좌표가 크거나 같다
            spot = home[i]    # 결과값 성립(가장 인접한 두 공유기 사이의 거리 유지)하면서 새로 공유기 설치 가능
            cnt += 1
    if cnt >= c:        # cnt 결과에 따라 mid 조정
        start_dis = mid_dis + 1
        result = mid_dis
    else:
        end_dis = mid_dis-1

print(result)






