# 인수의 생일 파티
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from heapq import heappush, heappop
from collections import deque

# BFS로 풀기
def BFS(start):
    queue = deque([start])  # 시작점 큐에 삽입
    while queue:
        v = queue.popleft()
        for node, weight in H[v]:
            if D[v] + weight < D[node]:
                D[node] = D[v] + weight
                queue.append(node)


# 다익스트라로 풀기
def Dijkstra(start):
    queue = []
    heappush(queue, (D[start], start))      # (출발점에서 거리, 정점 번호)
    while queue:
        dist, now = heappop(queue)
        # 정점 u의 최단 경로 확정
        if D[now] < dist:
            continue

        # 인접 정점을 찾아서, 간선 완화 작업 수행
        for node, weight in H[now]:
            if D[node] > D[now] + weight:
                D[node] = D[now] + weight
                heappush(queue, (D[node], node))


for tc in range(1, 1+int(input())):
    N, M, X = map(int, input().split())
    H = [[] for _ in range(N+1)]
    hours_lst = [0]
    for _ in range(M):
        x, y, c = map(int, input().split())
        H[x].append((y, c))

    for house in range(1, N+1):
        D = [0] + [1e9] * N; D[house] = 0
        #BFS(house)
        Dijkstra(house)
        hours_lst.append(D[X])

    D = [0] + [1e9] * N
    D[X] = 0
    #BFS(X)
    Dijkstra(X)
    for i in range(1, N+1):
        hours_lst[i] += D[i]

    print(f'#{tc}', max(hours_lst))





