# 5.8 DFS
# 그래프 인접 리스트 방식으로 구현, 노드를 나타내는 건 인덱스

def dfs(i, g, v):
    if v[i] == False:
        v[i] = True
        print(i, '번째 노드 방문')

        for n in g[i]:
            if v[n] == False:
                DFS(n, g, v)

graph = [
    [],    # 그래프 상에 0번째 노드가 없기 때문
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

dfs(1, graph, visit)