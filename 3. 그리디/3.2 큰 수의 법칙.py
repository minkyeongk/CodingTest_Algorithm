# 실전 3.2 큰 수의 문제
# M번 더하기, k번 연속 가능 (중간에 다른 숫자 끼면 다시 사용 가능)
# 입력 n m k / n개의 숫자
# 큰 수의 법칙에 따라 더해진 답을 출력

# 아이디어 고안: 큰 수를 최대한 많이 반복, 큰 수의 반복이 막히면 그 다음으로 큰 수...
#              정렬과 반복문을 이용하여 해결

# 띄어쓰기를 기준으로 정수형 자료 입력 받음
# map: 첫번째 인자인 자료형을 split한 각각의 input에 매핑
n, m, k = map(int, input().split())
list = list(map(int, input().split()))

list.sort()     # 기본 오름차순 정렬, 맨 뒤 값이 최대값
max = list[-1]
prior = list[-2]
cnt = 0         # cnt를 통해 단일 반복문으로 해결
sum = 0

# ver 1.
# 반복문과 조건문을 통한 해결
for i in range(m):
    if cnt == k:
        sum += prior
        cnt = 0
    else:
        sum += max
        cnt += 1

print(sum)

# ver 2.
# 반복되는 수열을 파악하여 수식으로 해결
sum2 = m//(k+1) * (max*k + prior) + m % (k+1) * max
print(sum2)



