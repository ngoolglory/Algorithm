# 그래프_최소 이동 거리
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque
from heapq import heappop, heappush

# BFS로 풀기
def BFS(r, c):
    queue = deque([(r, c)])  # 시작점 큐에 삽입
    while queue:
        r, c = queue.popleft()
        # 인접 정점을 찾아서, 간선 완화 작업 수행
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                weight = 1
                if arr[nr][nc] > arr[r][c]:
                    weight += arr[nr][nc] - arr[r][c]
                if D[nr][nc] > D[r][c] + weight:
                    D[nr][nc] = D[r][c] + weight
                    queue.append((nr, nc))


# DFS로 풀기 (틀림)
def DFS(r, c):
    if D[r][c] > D[N-1][N-1]: return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            weight = 1
            if arr[nr][nc] > arr[r][c]:
                weight += arr[nr][nc] - arr[r][c]
            if D[nr][nc] > D[r][c] + weight:
                D[nr][nc] = D[r][c] + weight
                DFS(nr, nc)


# 다익스트라로 풀기
def Dijkstra(r, c):
    queue = []
    heappush(queue, (D[r][c], (r, c)))      # (출발점에서 거리, 정점 번호)
    while queue:
        dist, now = heappop(queue)
        r, c = now
        # 정점 u의 최단 경로 확정
        if D[r][c] < dist:
            continue

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                weight = 1
                if arr[nr][nc] > arr[r][c]:
                    weight += arr[nr][nc] - arr[r][c]
                if D[nr][nc] > D[r][c] + weight:
                    D[nr][nc] = D[r][c] + weight
                    heappush(queue, (D[nr][nc], (nr, nc)))


for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    # D[v]: 출발점(s)에서 v까지 최단 경로의 가중치 합을 저장
    # 모든 정점에 대해 초기값은 아주 큰 값으로 설정 => 아직 어떤 경로도 발견하지 못함
    D = [[1e9] * N for _ in range(N)]
    # 가중치 그래프에서 BFS로 최단 경로를 구할 때 방문정보는 체크하지 않는다.
    D[0][0] = 0                    # 시작점의 거리는 0으로 설정
    #BFS(0, 0)
    DFS(0, 0)
    #Dijkstra(0, 0)

    print(f'#{tc}', D[N-1][N-1])
