# 5.5 두가지 방식으로 구현한 팩토리얼 예제
# 각각 재귀함수, 반복문으로 구현한 팩토리얼 함수

# 재귀함수로 구현
def factorialByRec(n):
    if n == 1:
        return 1
    return n * factorialByRec(n-1)

# 반복문으로 구현
def factorialByLoop(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

print('재귀함수 팩토리얼:', factorialByRec(5))
print('반복문 팩토리얼:', factorialByLoop(5))


