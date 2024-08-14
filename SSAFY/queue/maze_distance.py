# 큐_미로의거리_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def BFS(S):
    global visited
    queue = deque()             # 큐 생성
    queue.append(S)             # 시작점 enqueue
    visited[S[0]][S[1]] = 1     # 시작점 방문표시

    while queue:
        r, c = queue.popleft()         # dequeue

        if maze[r][c] == 3:            # dequeue 한 위치가 도착점이면
            # 누적합 방문 리스트를 통해 시작점으로부터의 거리 반환
            return visited[r][c] - 2   # -2 하는 이유는 출발점, 도착점을 세지 않기 때문

        # 동서남북 탐색
        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = r + dr
            nc = c + dc
            # 미로를 벗어나지 않고, 벽이 아니고, 방문한적 없는 위치면
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                queue.append((nr, nc))                  # 해당 위치 enqueue
                visited[nr][nc] = visited[r][c] + 1     # 해당 위치 누적합으로 방문 표시

    # 경로가 없는 경우 0 반환
    return 0


for tc in range(1, 1+int(input())):
    N = int(input())    # 미로 크기
    maze = [list(map(int, list(input()))) for _ in range(N)]    # 미로
    visited = [[0]*N for _ in range(N)]     # 방문 리스트

    # 출발 좌표 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                S = (r, c)

    answer = BFS(S)
    print(f'#{tc}', answer)