# 그래프_최소 이동 거리
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque
from heapq import heappop, heappush

# BFS로 풀기
def BFS(u):
    queue = deque([u])  # 시작점 큐에 삽입
    while queue:
        u = queue.popleft()
        # 인접 정점을 찾아서, 간선 완화 작업 수행
        for v, weight in G[u]:
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                queue.append(v)

# DFS로 풀기
def DFS(u):
    if D[u] > D[N]: return
    for v, weight in G[u]:
        if D[v] > D[u] + weight:
            D[v] = D[u] + weight
            DFS(v)


# 다익스트라로 풀기
def Dijkstra(u):
    queue = []
    heappush(queue, (D[u], u))      # (출발점에서 거리, 정점 번호)
    while queue:
        dist, now = heappop(queue)
        # 정점 u의 최단 경로 확정
        if D[now] < dist:
            continue

        # 인접 정점을 찾아서, 간선 완화 작업 수행
        for next, weight in G[now]:
            if D[next] > D[now] + weight:
                D[next] = D[now] + weight
                heappush(queue, (D[next], next))


for tc in range(1, 1+int(input())):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, weight = map(int, input().split())
        # s --weight--> e 간선
        G[s].append((e, weight))

    # D[v]: 출발점(s)에서 v까지 최단 경로의 가중치 합을 저장
    # 모든 정점에 대해 초기값은 아주 큰 값으로 설정 => 아직 어떤 경로도 발견하지 못함
    D = [1e9] * (N + 1)
    # 가중치 그래프에서 BFS로 최단 경로를 구할 때 방문정보는 체크하지 않는다.
    D[0] = 0                    # 시작점의 거리는 0으로 설정
    #BFS(0)
    #DFS(0)
    Dijkstra(0)

    print(f'#{tc}', D[N])