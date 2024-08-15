# 상호의 배틀필드
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

'''
<게임 맵의 구성 요소>
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
-----------------------------------------------------------------------------------------------
<사용자가 넣을 수 있는 입력의 종류>
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
'''

for tc in range(1, 1+int(input())):
    H, W = map(int, input().split())     # H: 맵의 높이 , W: 맵의 너비
    arr = [list(input()) for _ in range(H)]     # 맵
    N = int(input())                # 사용자가 넣을 입력의 개수
    command_lst = list(input())     # 사용자 명령 리스트
    
    # 전차의 현재 위치 좌표 찾기
    cur_r = cur_c = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c] in ['<','>','v','^']:
                cur_r, cur_c = r, c
    
    # 커맨드 하나씩 누르기
    for command in command_lst:
        
        # U 누름
        if command == 'U':
            arr[cur_r][cur_c] = '^'
            if arr[cur_r-1][cur_c] == '.':
                arr[cur_r][cur_c], arr[cur_r-1][cur_c] = arr[cur_r-1][cur_c], arr[cur_r][cur_c]
            
        # D 누름
        elif command == 'D':
            arr[cur_r][cur_c] = 'v'
            if arr[cur_r-1][cur_c] == '.':
                arr[cur_r][cur_c], arr[cur_r-1][cur_c] = arr[cur_r-1][cur_c], arr[cur_r][cur_c]
        
        # L 누름
        elif command == 'L':
            arr[cur_r][cur_c] = '<'
            if arr[cur_r-1][cur_c] == '.':
                arr[cur_r][cur_c], arr[cur_r-1][cur_c] = arr[cur_r-1][cur_c], arr[cur_r][cur_c]
        
        # R 누름
        elif command == 'R':
            arr[cur_r][cur_c] = '>'
            if arr[cur_r-1][cur_c] == '.':
                arr[cur_r][cur_c], arr[cur_r-1][cur_c] = arr[cur_r-1][cur_c], arr[cur_r][cur_c]
        
        # S 누름
        else:
            if arr[cur_r][cur_c] == '>':            # 오른쪽 바라보고 있음
                for c in range(cur_c+1, W):         # 오른쪽 끝까지 포탄 날아감
                    if arr[cur_r][c] == '*':        # 벽돌 만나면
                        arr[cur_r][c] = '.'
                        break
                    elif arr[cur_r][c] == '#':      # 강철벽 만나면
                        break
            elif arr[cur_r][cur_c] == '<':          # 왼쪽 바라보고 있음
                for c in range(cur_c-1, -1, -1):    # 왼쪽 끝까지 포탄 날아감
                    if arr[cur_r][c] == '*':        # 벽돌 만나면
                        arr[cur_r][c] = '.'
                        break
                    elif arr[cur_r][c] == '#':      # 강철벽 만나면
                        break
            elif arr[cur_r][cur_c] == '^':          # 위쪽 바라보고 있음
                for r in range(cur_r-1, -1, -1):    # 위쪽 끝까지 포탄 날아감
                    if arr[r][cur_c] == '*':        # 벽돌 만나면
                        arr[r][cur_c] = '.'
                        break
                    elif arr[r][cur_c] == '#':      # 강철벽 만나면
                        break
            elif arr[cur_r][cur_c] == 'v':          # 아래쪽 바라보고 있음
                for r in range(cur_r+1, H):         # 아래쪽 끝까지 포탄 날아감
                    if arr[r][cur_c] == '*':        # 벽돌 만나면
                        arr[r][cur_c] = '.'
                        break
                    elif arr[r][cur_c] == '#':      # 강철벽 만나면
                        break
    
    print(f'#{tc}', end=' ')
    for map_row in arr:
        print(''.join(map_row))