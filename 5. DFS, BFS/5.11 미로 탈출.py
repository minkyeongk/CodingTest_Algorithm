# 5.11 미로 탈출

from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
c, r = 0, 0
Q = deque()

while True:
    if c == n-1 and r == m-1:
        break

    for t in d:
        nc = c + t[0]
        nr = r + t[1]
        if nc < 0 or nc > n-1 or nr < 0 or nr > m-1:
            continue

        if maze[nc][nr] == 1:
            Q.append((nc, nr))
            maze[nc][nr] = maze[c][r]+1

    c, r = Q.popleft()

print(maze[n-1][m-1])
