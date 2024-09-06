# 정사각형 방
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

# bfs로 풀기
from collections import deque

def bfs(r, c):
    max_cnt = 0
    queue = deque()
    queue.append((r, c, arr[r][c], 1))
    while queue:
        r, c, num, cnt = queue.popleft()
        memo[r][c] = 1
        max_cnt = max(max_cnt, cnt)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == num + 1:
                queue.append((nr, nc, num+1, cnt+1))
                break
    return max_cnt

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    ans_num = 0
    ans_cnt = 0
    memo = [[0] * N for _ in range(N)]         # 지나온 곳 메모할 메모장
    for r in range(N):
        for c in range(N):
            if not memo[r][c]:
                max_cnt = bfs(r, c)
                if max_cnt > ans_cnt:
                    ans_cnt = max_cnt
                    ans_num = arr[r][c]
                elif max_cnt == ans_cnt and arr[r][c] < ans_num:
                    ans_num = arr[r][c]
    print(f'#{tc}', ans_num, ans_cnt)

# ================================================================

# 반복문으로 풀기
for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    for r in range(N):
        for c in range(N):
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                    visited[arr[r][c]] = 1
                    break

    cnt = max_cnt = start = 0
    for i in range(len(visited)-1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if cnt >= max_cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0

    print(f'#{tc}', start, max_cnt + 1)