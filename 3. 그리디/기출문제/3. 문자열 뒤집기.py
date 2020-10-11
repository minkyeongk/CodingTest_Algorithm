s = input()

znum = 0
onum = 0
pre = s[0]

for i in range(len(s)):
    if i != 0:
        if pre == s[i]:
            pre = s[i]
            continue

    if s[i] == '0':
        znum += 1
    else:
        onum += 1
    pre = s[i]

print(min(znum, onum))