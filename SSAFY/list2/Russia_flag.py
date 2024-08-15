# 러시아 국기 같은 깃발 
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())            # N행 M열
    arr = [list(input()) for _ in range(N)]     # 배열
    
    # N개를 3분할하는 모든 경우의 수 구하기 (조합)
    boundary = []
    for i in range(1, N-1):
        for j in range(i+1, N):
            boundary.append((i, j))
    
    min_coloring = float('inf')
    
    # 각 경우의 수에 대해 순회
    for i, j in boundary:
        need_coloring = 0   # 새로 칠해야하는 칸의 개수
        
        for r in range(N):
            for c in range(M):
                
                # 흰색 영역
                if r < i:
                    if arr[r][c] != 'W':    # 흰색이 아니면
                        need_coloring += 1
                
                # 파란색 영역
                elif r < j:
                    if arr[r][c] != 'B':    # 파란색이 아니면
                        need_coloring += 1
                
                # 빨간색 영역
                else:
                    if arr[r][c] != 'R':    # 빨간색이 아니면
                        need_coloring += 1
                        
        # 현재 케이스에서 새로 칠해야하는 칸의 개수가 최솟값보다 작으면 갱신
        if need_coloring < min_coloring:
            min_coloring = need_coloring
    
    print(f'#{tc}', min_coloring)