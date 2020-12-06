# 35. 못생긴 수
# 앞에서부터 하나씩 2도 곱하고 3도 곱하고 5도 곱하고
# 모든 수에 2, 3, 5가 다 곱해지되, 곱해졌는지 여부를 인덱스 저장으로 나타내주기

n = int(input())

# 인덱스를 저장할거니까 인덱스 접근 중에 에러가 나지 않도록 리스트를 채워 초기화
table = [1] * n

i2 = i3 = i5 = 0  # 이 인덱스의 숫자에 각 숫자가 곱해졌는지를 나타냄
m2, m3, m5 = 2, 3, 5

for j in range(1, n):
    table[j] = min(m2, m3, m5)
    # elif 가 아니라 if로 처리하는 이유는 m2인 동시에 m3일 때 if문을 둘다 거치면서 중복된 수가 나오지 않도록 하기 위해
    if table[j] == m2:
        i2 += 1
        m2 = table[i2]*2
    if table[j] == m3:
        i3 += 1
        m3 = table[i3]*3
    if table[j] == m5:
        i5 += 1
        m5 = table[i5]*5

print(table[n-1])





