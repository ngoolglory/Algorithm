# 완전검색_최소합
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def backtrack(idx, pos, total_v):
    global min_v

    if total_v >= min_v:                    # 현재 경로 가는 중에 총합이 최소 합을 이미 넘었으면
        return                              # 이 경로는 최소값이 될 가능성이 없음 (가지치기)
    
    if idx == (2*N - 1):                    # 최대 경로 길이까지 도달했다면
        min_v = min(min_v, total_v)         # 현재 경로 합과 최소 합을 비교해서 최소 합 갱신 
        return

    for k in range(2):
        nr = pos[0] + dr[k]
        nc = pos[1] + dc[k]
        if nr < N and nc < N:
            backtrack(idx + 1, [nr, nc], total_v + arr[nr][nc])


for tc in range(1, int(input())+1):
    N = int(input())                                                # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]       # 배열
    dr = [0, 1]; dc = [1, 0]                                        # 델타 값 (우, 하)
    min_v = 13 * (2*N - 1)                                          # 최소 합 초기 값

    backtrack(1, [0, 0], arr[0][0])
    print(f'#{tc}', min_v)