# 6.8 정렬 라이브러리 키 기준 정렬 예제

arr = [('가을', 2), ('겨울', 5), ('봄', 3)]

print(sorted(arr, key=lambda x: x[1]))
