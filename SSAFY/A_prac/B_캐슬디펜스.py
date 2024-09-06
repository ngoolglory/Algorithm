# 캐슬 디펜스
'''
- 각 칸에 포함된 적의 수는 최대 하나
- N+1번 행의 모든 칸에는 성이 있음
- 궁수는 성이 있는 칸에 3명만 배치
- 하나의 칸에는 최대 1명의 궁수만 있을 수 있음
- 각 턴마다 궁수는 적 하나 공격, 모든 궁수는 동시에 공격
- 궁수는 가장 가까운 적을 공격하고, 같은 거리에 적이 여럿 있으면 왼쪽 적 공격
- 같은 적이 여러 궁수에게 공격 당할 수 있음
- 궁수 공격 끝나면 적 이동 (아래로 한 칸)
- 적이 성이 있는 칸으로 이동한 경우 게임에서 제외
- 모든 적이 격자 판에서 제외되면 게임 끝
goal : 궁수의 공격으로 제거할 수 있는 적의 최대 수
0 : 빈 칸
1 : 적이 있는 칸
'''

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#input = sys.stdin.readline

def BFS(archer):
    arr_copy = deepcopy(arr)                                    # 격자 깊은 복사 
    visited = [[0] * M for _ in range(N)]                       # 방문 처리
    kill = 0                                                    # 킬 카운트
    for pos_r in range(N-1, -1, -1):                            # 한 칸씩 전진(적이 아닌 궁수가 전진)
        die = []
        for pos_c in archer:                                    # 궁수 한명씩 차례로 쏴보자
            queue = deque()                                 
            queue.append([pos_r, pos_c, 1])                     # 현재 행, 열, 거리 정보 큐에 넣기
            while queue:
                r, c, d = queue.popleft()
                if arr_copy[r][c]:
                    die.append([r, c])
                    if not visited[r][c]:
                        visited[r][c] = 1
                        kill += 1                               # 죽였으니 점수 증가
                    break

                if d < D:                                       # 사정거리보다 짧으면
                    for k in range(3):                          # 좌 상 우 순서로 탐색
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < N and 0 <= nc < M:
                            queue.append([nr, nc, d+1])         # 거리 증가

        for r, c in die:                                        # 모든 궁수가 동시에 공격하니 마지막에 처리
            arr_copy[r][c] = 0

    return kill

N, M, D = map(int, input().split())             # N: 격자판 행 수, M: 격자판 열 수, D: 궁수 공격 거리 제한
arr = [list(map(int, input().split())) for _ in range(N)]   # 격자 판
dr, dc = [0, -1, 0], [-1, 0, 1]                         # 좌 상 우 (같은 거리에 적이 있으면 가장 왼쪽 적 우선 공격)
max_kill = 0
for archer in combinations([i for i in range(M)], 3):   # nC3 궁수 자리 경우의 수
    max_kill = max(max_kill, BFS(archer))
print(max_kill)