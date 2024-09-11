# 그래프_최소 신장 트리
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from heapq import heappop, heappush

def prim(start):
    heap = []
    MST = [0] * (V+1)
    sum_weight = 0
    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)

        # 이미 방문한 지점이면 통과
        if MST[v]: continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드를 보면서
        for next in range(V+1):
            # 갈 수 없는 지점이면 통과
            if graph[v][next] == 0: continue
            # 이미 방문한 지점이면 통과
            if MST[next]: continue
            heappush(heap, (graph[v][next], next))

    return sum_weight


for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    print(f'#{tc}', prim(0))