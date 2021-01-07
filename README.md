# CodingTest_Algorithm
"이것이 취업을 위한 코딩 테스트다" 알고리즘 문제 풀이 코드 모음

관련 링크: https://github.com/ndb796/python-for-coding-test

9. 최단 경로: 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘
최단 경로 알고리즘은 보통 그래프로 표현 (V > vertex, E > edge)


     1) 다익스트라 알고리즘
        하나의 특정 노드에서 출발하여 나머지 노드들로 가는 각각의 최단 경로를 구하는 알고리즘
        => 출발지는 하나, 도착지는 나머지 모두 > 고로 최단 거리는 나머지 모두 만큼의 개수
        매번 비용이 가장 적은 노드를 선택 > 그리디 알고리즘
        graph(인접 리스트), table(최단 거리 테이블), visit(방문 여부 테이블, 힙 사용시 필요 없음)로 구성   
        
        (1) 출발 노드를 설정한다
        (2) 최단 거리 테이블을 초기화 한다 (출발노드는 0, 나머지는 무한)
        (3) 방문하지 않은 노드 중에 출발지로부터의 최단 거리가 가장 짧은 노드를 선택한다
        (4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
        (5) (3)과 (4)를 반복한다

        한 단계당 하나의 노드에 대한 최단 거리를 확실히 함 (그 단계에서 최단 거리 노드로 선택된 노드)
        
        간단하게 구현할 경우: 매 단계마다 최단 거리 테이블과 방문 여부 테이블을 확인하여 노드 선택, 시간 복잡도 O(V^2)
        개선하여 구현할 경우: 최단거리 테이블 대신 최소힙 사용, 현재 최단 거리 테이블과 힙에서 꺼낸 값을 비교하여 방문 여부를 확인하고 노드 선택
        (이미 자기보다 작은 값으로 확정이 되어있는 경우, 해당 값으로의 갱신은 이미 이전에 힙에서 다른 값을 꺼내 이루어짐,
        최소힙으로 인해 중복되는 노드 중 가장 작은 값으로 이미 확정이 되어있을 것이므로) 시간 복잡도 O(ElogV)
        ※ 시간 복잡도 계산: E개의 간선을 힙에 넣었다 빼는 연산 O(ElogE) (logE인 연산을 E번 반복)
                          E <= V^2, logE == log(V^2) == 2logV
                          따라서 ElogE == 2ElogV, 결과: O(ElogV)

    2) 플로이드 워셜 알고리즘
        모든 지점에서 다른 모든 지점(본인 제외)까지의 최단 경로를 구하는 알고리즘
        거쳐가는 노드를 기준으로 알고리즘 수행, 출발지에서 특정 노드를 거쳐 도착지까지 가는 비용과 기존의 비용을 비교
        graph(인접 행렬) 사용
        연결된 간선은 값으로, 연결되지 않은 간선은 무한으로 초기화 > n번의 단계를 반복하며 점화식에 맞게 인접 행렬 갱신(DP)

        점화식: D_ab = min(D_ab, D_ak + D_kb)
        => 출발지 n개, 각 출발지마다 도착지 n-2개 (본인, 거쳐가는 노드 총 2개) n*(n-1)*(n-2) (출발지, 거쳐가는 노드, 도착지)
        시간 복잡도 O(n^3)