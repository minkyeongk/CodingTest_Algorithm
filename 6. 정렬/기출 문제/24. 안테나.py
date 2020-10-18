# 24. 안테나
# 길게 푼거 같아서 정답 코드 확인해보기
n = int(input())
home = list(map(int, input().split()))
home.sort()
mid_idx = n//2

def get_distance(home, mid):
    dis = 0
    for h in home:
        dis += abs(h-home[mid])
    return dis

dis = [1e9]*n
dis[mid_idx] = get_distance(home, mid_idx)
# 양 옆값이랑 비교, 제일 작은 값으로 옮겨간다
while True:
    list = []
    if mid_idx-1 >= 0:
        dis[mid_idx-1] = dis[mid_idx-1] if dis[mid_idx-1] != 1e9 else get_distance(home, mid_idx-1)
        list.append(dis[mid_idx-1])
    if mid_idx + 1 < n:
        dis[mid_idx + 1] = dis[mid_idx + 1] if dis[mid_idx + 1] != 1e9 else get_distance(home, mid_idx + 1)
        list.append(dis[mid_idx + 1])
    temp = min(list)
    if temp == dis[mid_idx]:
        if temp == dis[mid_idx-1]:
            print(home[mid_idx-1])
        else:
            print(home[mid_idx])
        break
    elif temp == dis[mid_idx-1]:
        mid_idx -= 1
    else:
        mid_idx += 1









