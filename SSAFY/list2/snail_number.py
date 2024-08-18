# 달팽이 숫자

# 델타 값 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())                    # 달팽이 크기
    arr = [[0]*N for _ in range(N)]     # 배열 생성
    
    dir = 0                             # 방향 정보
    cnt = 0
    r, c = 0, -1
    while cnt < N**2:
        nr, nc = r + dr[dir], c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            cnt += 1
            r, c = nr, nc
            arr[r][c] = cnt
        else:
            dir = (dir + 1) % 4
    
    print(f'#{tc}')
    for line in arr:
        print(*line)