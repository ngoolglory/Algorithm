# [S/W 문제해결 응용] 4일차 - 보급로
import sys
import heapq
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")


def dijkstra():
    global distance
    pq = []
    dist = arr[0][0]
    heapq.heappush(pq, (dist, 0, 0))

    while pq:
        dist, r, c = heapq.heappop(pq)
        
        if distance[r][c] < dist:
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nxt_dist = dist + arr[nr][nc]
                if nxt_dist < distance[nr][nc]:
                    distance[nr][nc] = nxt_dist
                    heapq.heappush(pq, (nxt_dist, nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input().strip()))) for _ in range(N)]
    distance = [[int(1e9)] * N for _ in range(N)]

    dijkstra()

    print(f'#{tc} {distance[N-1][N-1]}')