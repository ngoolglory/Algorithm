# 풍선팡
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 행 수, M: 열 수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열
    max_flowers = float('-inf')     # 꽃가루 합 최대값
    
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for r in range(N):
        for c in range(M):
            flower_sum = arr[r][c]  # 꽃가루 개수 초기값은 현재 위치
            for k in range(4):      # 상하좌우
                for n in range(1, arr[r][c]+1):     # 현재 위치 꽃가루 개수만큼 터뜨리기
                    nr = r + dr[k]*n
                    nc = c + dc[k]*n
                    # 유효한 위치면
                    if 0 <= nr < N and 0 <= nc < M:
                        flower_sum += arr[nr][nc]   # 합에 더하기
            # 꽃가루 합이 기존 최대값보다 크면 갱신
            if flower_sum > max_flowers:
                max_flowers = flower_sum
                
    print(f'#{tc}', max_flowers)