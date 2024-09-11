# [S/W 문제해결 응용] 4일차 - 하나로
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from heapq import heappop, heappush

def prim(start):
    heap = []
    MST = [0] * N
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
        for next in range(N):
            # 자기 자신이면 통과
            if graph[v][next] == 0: continue
            # 이미 방문한 지점이면 통과
            if MST[next]: continue
            heappush(heap, (graph[v][next], next))

    return sum_weight


for tc in range(1, 1+int(input())):
    N = int(input())        # 섬의 개수
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())      # 환경 부담 세율 실수

    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = E * ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)

    print(f'#{tc}', round(prim(0)))

