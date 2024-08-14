# 큐_노드의거리_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def BFS(S, G):
    global visited
    queue = deque()     # 큐 생성
    queue.append(S)     # 시작 노드 enqueue
    visited[S] = 1      # 시작 노드 방문 표시 (자기 자신 거리 1로 시작)

    while queue:
        v = queue.popleft()         # dequeue
        if v == G:                  # dequeue 한 노드가 도착 노드이면
            return visited[v] - 1   # 자기 자신 거리를 1로 시작했기 때문에 1뺀 거리 반환
        for i in adj_l[v]:          # dequeue 한 노드의 인접 노드 탐색
            if not visited[i]:      # 아직 방문 안한 노드면
                queue.append(i)     # enqueue
                visited[i] = visited[v] + 1     # 방문 표시와 동시에 시작 노드로부터의 거리 계산

    # 출발 노드와 도착 노드가 연결되어 있지 않으면 0 반환
    return 0


for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())    # V: 노드 개수, E: 간선 개수
    adj_l = [[] for _ in range(V+1)]    # 인접 리스트 생성
    visited = [0] * (V+1)           # 방문 리스트 생성

    # 인접 리스트 채우기
    for _ in range(E):
        n1, n2 = map(int, input().split())    # 노드 2개
        # 양방향 연결
        adj_l[n1].append(n2)
        adj_l[n2].append(n1)

    # 출발 노드, 도착 노드 받기
    S, G = map(int, input().split())

    answer = BFS(S, G)
    print(f'#{tc}', answer)