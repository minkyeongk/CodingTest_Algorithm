# 시도 중..
n, l, r = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))
whole = []      # 연합 내용을 모아놓은 리스트

def chk(origin, new):
    global whole
    for i in range(len(whole)):
        if origin in whole[i]:
            whole[i].append(new)
            return
    whole.append([origin, new])

result = 0
while True:
    print(result, "시도")
    flag = 0
    for i in range(n):
        for j in range(n):
            if j+1 < n:
                if l <= abs(table[i][j]-table[i][j+1]) <= r:
                    chk((i, j), (i, j+1))
                    flag = 1
            if i+1 < n:
                if l <= abs(table[i][j]-table[i+1][j]) <= r:
                    chk((i, j), (i+1, j))
                    flag = 1
    print(whole)
    for i in range(len(whole)-1):
        for j in range(i+1, len(whole)):
            print(i, j)
            if j < len(whole):
                for con in whole[i]:
                    print(con)
                    if con in whole[j]:
                        whole.append(list(set(whole[i]+whole[j])))
                        whole.remove(whole[i])
                        whole.remove(whole[j])
                        break

    if flag == 0:
        print(result)
        break

    for uni in whole:
        sum = 0
        for i in uni:
            sum += table[i[0]][i[1]]
        temp = sum // len(uni)
        for j in uni:
            table[j[0]][j[1]] = temp
        result += 1

    for k in range(n):
        print(table[k])
    whole.clear()




