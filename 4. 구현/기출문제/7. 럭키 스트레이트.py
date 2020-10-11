# 7. 럭키스트레이트
# 쉬운 문제일수록 차근차근 풀기

n = input()
l = len(n)//2
left, right = 0, 0
for i in range(l):
    left += int(n[i])
    right += int(n[l+i])

if left == right:
    print("LUCKY")
else:
    print("READY")
