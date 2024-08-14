# [S/W 문제해결 기본] 7일차 - 미로1
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def BFS(maze, start):
    queue = deque()     # 큐 생성
    # 델타
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    # 시작 좌표 큐에 넣기
    queue.append((start[0], start[1]))

    # 길이 막힐 때까지 가
    while queue:
        r, c = queue.popleft()

        for k in range(4):              # 동서남북
            # 만약 동서남북 중에 하나라도 뚫려있는 곳이 있으면 갈 수 있는 길
            nr = r + dr[k]
            nc = c + dc[k]
            # 유효한 위치이면
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:       # 도착 지점이면
                    return 1                # 도달 가능!! (1)
                maze[nr][nc] = 1            # 1로 색칠하면서 가기
                queue.append((nr, nc))      # 해당 좌표 큐에 추가

    # 한번도 3을 못찾았으면
    return 0        # 도달 불가!! (0)


for _ in range(10):
    tc = int(input())       # 테스트케이스
    maze = [list(map(int, list(input()))) for _ in range(16)]

    # 시작점 찾기
    start = 0
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                start = (r, c)
                break

    answer = BFS(maze, start)
    print(f'#{tc}', answer)