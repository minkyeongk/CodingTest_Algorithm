# 8. 문자열 재정렬
# 숫자 담는 리스트, 알파벳 담는 리스트 만들어서 정렬해서 붙여서 출력

origin = input()

alpha = []
sum = 0
for i in range(len(origin)):
    if origin[i].isdigit():
        sum += int(origin[i])
    else:
        alpha.append(origin[i])

print("".join(sorted(alpha))+str(sum))
