# [모의 SW 역량테스트] 탈주범 검거
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def BFS(r, c):
    global cnt
    queue = deque()
    queue.append((r, c, 1))
    visited[r][c] = 1
    cnt += 1
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in move[arr[r][c]]:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not arr[nr][nc]:
                continue
            if visited[nr][nc]:
                continue
            if time >= L:
                continue
            for ddr, ddc in move[arr[nr][nc]]:
                if nr + ddr == r and nc + ddc == c:
                    queue.append((nr, nc, time + 1))
                    visited[nr][nc] = time
                    cnt += 1
                    break


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    move = [[],
            [(1,0),(-1,0),(0,1),(0,-1)],
            [(1,0),(-1,0)],
            [(0,1),(0,-1)],
            [(-1,0),(0,1)],
            [(1,0),(0,1)],
            [(0,-1),(1,0)],
            [(-1,0),(0,-1)]]
    cnt = 0
    BFS(R, C)

    print(f'#{tc}', cnt)