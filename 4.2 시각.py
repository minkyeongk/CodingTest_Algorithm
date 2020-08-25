# 예제 4.2 시각
# 입력 n
# 출력 3이 포함되는 모든 경우의 수

# 모든 경우의 수를 다 봐야 하는 완전 탐색

cnt = 0
n = int(input())

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                cnt += 1

print(cnt)
