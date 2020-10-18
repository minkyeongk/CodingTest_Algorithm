# 19. 연산자 끼워넣기
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
result = []

def calcul(a, op, nowop, now, idx):
    global n, result
    newop = [x for x in op]
    if nowop == 0:
        now += a[idx]
        newop[0] -= 1
    elif nowop == 1:
        now -= a[idx]
        newop[1] -= 1
    elif nowop == 2:
        now *= a[idx]
        newop[2] -= 1
    elif nowop == 3:        # 음수 계산 경우 나눠줘야
        now = now//a[idx] if now >= 0 else -((-now)//a[idx])
        newop[3] -= 1

    #print(now)
    if idx == n-1:
        result.append(now)
        #print("계산된 인덱스", idx, "추가된 결과", now)
        return

    for i in range(4):
        if newop[i] != 0:
            #print(now, "호출", idx+1)
            #print(i, newop)
            calcul(a, newop, i, now, idx+1)


for i in range(4):
    if op[i] != 0:
        calcul(a, op, i, a[0], 1)
        #print(i, "차 호출")

#print(result)
print(max(result))
print(min(result))
