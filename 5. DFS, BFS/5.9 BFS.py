# 5.9 BFS
# 그래프 인접 리스트 방식으로 구현, 노드를 나타내는 건 인덱스
from collections import deque


def bfs(i, g, v):
    Q = deque()
    if not v[i]:
        v[i] = True
        print(i, '번째 노드 방문')
        Q.append(i)

    # 큐가 비면 더이상 노드를 꺼낼 수 없으니까
    while Q:
        n = Q.popleft()
        for j in range(len(g[n])):
            ad = g[n][j]
            if not v[ad]:
                v[ad] = True
                print(ad, '번째 노드 방문')
                Q.append(ad)


graph = [
    [],  # 그래프 상에 0번째 노드가 없기 때문
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

bfs(1, graph, visit)
