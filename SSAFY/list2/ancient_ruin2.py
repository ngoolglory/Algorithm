# 고대유적2
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 행 개수, M: 열 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 0]
    dc = [0, 1]
    max_cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                for k in range(2):
                    cnt = 1
                    for n in range(1, max(N, M)):
                        nr = r + dr[k]*n
                        nc = c + dc[k]*n
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                            cnt += 1
                        else:
                            break
                    if cnt > 1 and cnt > max_cnt:
                        max_cnt = cnt
    print(f'#{tc}', max_cnt)