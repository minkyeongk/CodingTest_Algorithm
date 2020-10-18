from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

def chicken_dis(home, mchick):
    result = 0
    for h in home:
        each = 1e9
        for chk in mchick:
            temp = abs(h[0]-chk[0]) + abs(h[1]-chk[1])
            each = min(temp, each)
        result += each
    return result

final = 1e9
for com in combinations(chicken, m):
    final = min(final, chicken_dis(home, com))

print(final)
