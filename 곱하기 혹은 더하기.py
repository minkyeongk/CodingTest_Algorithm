temp = input()
arr = []
for i in temp:
    arr.append(int(i))

n = arr[0]
if n == 1 or n == 0:
    flag = '+'
else:
    flag = '*'

for i in range(1, len(arr)):
    if flag == '+':
        n += arr[i]
        flag = '*'
        continue

    if arr[i] == 0 or arr[i] == 1:
        n += arr[i]
    else:
        n *= arr[i]

print(n)

