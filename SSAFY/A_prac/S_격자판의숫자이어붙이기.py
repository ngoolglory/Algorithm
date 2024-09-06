# 격자판의 숫자 이어 붙이기
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

# dfs로 풀기
def dfs(r, c, string):
    if len(string) == 7:
        memo.add(string)
        return
    else:
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, string + arr[nr][nc])


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    memo = set()        # 길이 7의 중복되지 않은 문자열 저장

    for r in range(4):
        for c in range(4):
            dfs(r, c, arr[r][c])
    
    print(f'#{tc}', len(memo))

# ============================================================

# bfs로 풀기
from collections import deque

def bfs(r, c, string):
    queue = deque()
    queue.append((r, c, string))
    while queue:
        r, c, string = queue.popleft()
        if len(string) == 7:
            memo.add(string)
        else:
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    queue.append((nr, nc, string + arr[nr][nc]))


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    memo = set()        # 길이 7의 중복되지 않은 문자열 저장

    for r in range(4):
        for c in range(4):
            bfs(r, c, arr[r][c])
    
    print(f'#{tc}', len(memo))