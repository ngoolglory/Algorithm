import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

'''
1. 출발지점, 도착지점 찾기
2. 스택에 현재 좌표 넣기
3. 스택에서 현재 좌표 pop
4. 주변에 갈 수 있는 곳 찾기
5. 갈 수 있으면 스택에 추가 후, 방문 표시
6. 갈 수 없으면 다시 처음으로 돌아가 마지막으로 방문한 좌표 스택에서 pop
   => 다시 갈 수 있는 곳 찾기 반복
7. 반복문이 끝난 후 목표 지점에 방문했는지 안했는지 검사
'''

def f_maze(N, maze):
    stack = []
    visited = [[False] * N for _ in range(N)]  # 방문 리스트
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    # 출발 지점, 도착 지점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                s_r = r
                s_c = c
            elif maze[r][c] == 3:
                e_r = r
                e_c = c

    # 출발 좌표 스택에 넣기
    stack.append((s_r, s_c))

    # 목표지점 도달 or 갈 곳이 없을 때까지 반복
    while stack:
        r, c = stack.pop()      # 스택에서 현재 좌표 pop
        for i in range(4):      # 동서남북 좌표
            nr = r + dr[i]
            nc = c + dc[i]
            # 도착 지점에 도달하면 1 반환
            if nr == e_r and nc == e_c:
                return 1
            # 가려는 위치가 벽이 아니면서 방문한 적이 없으면
            if 0<=nr<N and 0<=nc<N and maze[nr][nc] == 0 and not visited[nr][nc]:
                stack.append((nr, nc))      # 스택에 추가 후
                visited[nr][nc] = True      # 방문 표시

    return 0


for tc in range(1, int(input())+1):
    N = int(input())                                        # 미로의 크기 (N*N)
    maze = [list(map(int, input())) for _ in range(N)]      # 미로

    # 도착할 수 있는지 확인 (도착할 수 있으면 1, 아니면 0)
    answer = f_maze(N, maze)
    print(f'#{tc}', answer)