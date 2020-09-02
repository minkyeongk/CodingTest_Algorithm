# 5.4 재귀함수의 종료 조건 예제
# 종료 조건이 있는 재귀함수, 100번 호출하는 재귀함수

def recursive(i):
    if i == 100:
        print('100번째 호출!')
        print(i, '번째 함수 종료')
        return
    print('아직', 100-i, '번 남았다..!')
    recursive(i+1)
    print(i, '번째 함수 종료')

recursive(1)
