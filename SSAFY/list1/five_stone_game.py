import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def check_five_stone(N, arr):
    # 우 / 하 / 우하 / 좌하
    dr = [0, -1, -1, -1]
    dc = [1, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':    # 'o'를 만나면
                for k in range(4):      # 델타
                    continuous_num = 1
                    for n in range(1, 5):      # 현재 돌 포함 연속 4번
                        nr = r + dr[k]*n
                        nc = c + dc[k]*n
                        # 유효한 좌표면
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                continuous_num += 1
                            else:
                                break
                            if continuous_num == 5:
                                return 'YES'
    
    return 'NO'
    

for tc in range(1, 1+int(input())):
    N = int(input())    # N: 판 크기
    arr = [list(input()) for _ in range(N)]     # 판
    answer = check_five_stone(N, arr)
    print(f'#{tc}', answer)