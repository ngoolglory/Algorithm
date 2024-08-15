# [S/W 문제해결 기본] 5일차 - Magnetic
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 11):
    N = int(input())    # 테이블 사이즈
    arr = [list(map(int, input().split())) for _ in range(N)]    # 테이블
    cnt = 0             # 교착 상태 개수
    
    # 각 열을 위에서부터 읽어 내려가면서 N 나오고 그 다음 S나오면 cnt + 1
    for c in range(N):
        get_N = False           # N이 나왔는지
        for r in range(N):
            if arr[r][c] == 1:  # N 나왔어
                get_N = True
            elif arr[r][c] == 2 and get_N:  # S가 나왔고, 앞전에 N이 나왔으면
                cnt += 1
                get_N = False
                
    print(f'#{tc}', cnt)