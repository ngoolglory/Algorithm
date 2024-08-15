# 재미있는 오셀로 게임 
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 보드 크기, M: 돌 놓는 횟수
    arr = [[0]*N for _ in range(N)]     # 배열
    
    # 배열 초기 배치 상태 만들기
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 2
    arr[N//2][N//2-1] = arr[N//2-1][N//2] = 1
    
    # 델타
    dr = [0, 0, 1, -1, 1, 1, -1, -1]
    dc = [1, -1, 0, 0, 1, -1, 1, -1]
    
    for _ in range(M):
        # 1: 흑, 2: 백  (3에서 color 빼면 반대 색 나옴)
        c, r, color = map(int, input().split())
        # 좌표 보정
        c -= 1; r -= 1
        # 해당 지점 돌 놓기
        arr[r][c] = color
        
        # 상하좌우 돌 확인
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            # 반대 색이 있으면
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 3-color:
                # 그 다음 칸들에 놓을 돌이랑 같은 색이 있는지 확인
                cnt = 0     # 몇칸 갔는지
                for n in range(N):
                    cnt += 1            # 한칸 갔어
                    nnr = nr + dr[k]*n
                    nnc = nc + dc[k]*n
                    # 배열 범위 내에 있으면
                    if 0 <= nnr < N and 0 <= nnc < N:
                        # 같은 색을 만나면
                        if arr[nnr][nnc] == color:
                            # 온 만큼 뒤로가면서 뒤집기
                            for nn in range(1, cnt+1):
                                # 사이에 있는 돌 뒤집기
                                arr[nnr+dr[k]*(-nn)][nnc+dc[k]*(-nn)] = color
                            break
                        # 0을 만나면 이 방향은 뒤집을 돌 없어
                        elif arr[nnr][nnc] == 0:
                            break
                    # 배열 범위를 벗어나면 이 방향은 뒤집을 돌 없어
                    else:
                        break
    
    # 게임 끝난 후 보드 위의 흑돌, 백돌 개수 구하기
    white_cnt = 0
    black_cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                black_cnt += 1
            elif arr[r][c] == 2:
                white_cnt += 1
    
    # 흑돌, 백돌 개수 출력
    print(f'#{tc}', black_cnt, white_cnt)