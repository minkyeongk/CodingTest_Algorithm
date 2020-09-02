# 실전 3.4 1이 될 때까지
# n이 1이 될때까지 n에서 1을 빼거나, n을 k로 나눈다 (n이 k로 나누어 떨어질 때)
# 입력 n, k
# 출력 연산의 최소 횟수

# 아이디어: k로 나누는 것이 1을 빼는 것보다 값이 작아지는 속도가 빠름, 가능하면 무조건 나누기

n, k = map(int, input().split())
cnt = 0

while n != 1:
    n = (n//k if n % k == 0 else n-1)
    cnt += 1

print(cnt)


