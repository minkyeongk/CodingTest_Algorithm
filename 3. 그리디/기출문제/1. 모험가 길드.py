n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
table = [0] * n

for i in range(n):
    pt = i
    temp = -1
    while pt < n:
        temp += arr[pt]
        if temp < n:
            table[i] += 1
            pt = temp
        else:
            pt += 1

print(max(table))

