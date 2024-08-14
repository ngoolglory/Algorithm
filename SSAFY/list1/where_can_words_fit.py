import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def can_words_fit(N, K, arr):
    perfect_pos_num = 0     # 딱 K칸인 위치 개수
    
    # 우, 하
    dr = [0, 1]
    dc = [1, 0]
    
    # 가로 탐색
    for r in range(N):
        # 새로운 행으로 들어오면 탐색 기록 다시 초기화
        already_check = False
        
        for c in range(N):
            # 검은 색 만나면 탐색 기록 초기화
            if not arr[r][c]:   
                already_check = False
                
            if already_check:   # 아까 전에 이미 탐색 했으면
                continue        # 그냥 넘어가
            
            if arr[r][c]:       # 흰색 부분에 도달하면
                already_check = True    # 탐색 기록
                # 우 방향에 대해서 탐색
                white_len = 1           # 연속으로 나오는 흰색 칸의 수
                
                # 왜 K+1이냐면 딱 K칸 있어야하는데 그거보다 많은 경우를 배제하려고
                for n in range(1, K+1):     # 지금 현재 위치 + K번째까지 확인     
                    nr = r + dr[0]*n
                    nc = c + dc[0]*n
                    # 유효한 위치이면 (arr를 벗어나지 않고, 검은 칸이 아닐 때)
                    if 0 <= nc < N and arr[nr][nc]:
                        white_len += 1
                    # 유효하지 않은 위치이면
                    else:
                        # 지금까지 연속으로 나온 흰색 칸수가 K개인지 확인
                        if white_len == K:          # 딱 K개면
                            perfect_pos_num += 1    # 최종 자리 개수 + 1
                        break
    
    # 세로 탐색
    for c in range(N):
        # 새로운 열로 들어오면 탐색 기록 다시 초기화
        already_check = False
        
        for r in range(N):
            # 검은 색 만나면 탐색 기록 초기화
            if not arr[r][c]:   
                already_check = False
                
            if already_check:   # 아까 전에 이미 탐색 했으면
                continue        # 그냥 넘어가
            
            if arr[r][c]:       # 흰색 부분에 도달하면
                already_check = True    # 탐색 기록
                # 우 방향에 대해서 탐색
                white_len = 1           # 연속으로 나오는 흰색 칸의 수
                
                # 왜 K+1이냐면 딱 K칸 있어야하는데 그거보다 많은 경우를 배제하려고
                for n in range(1, K+1):     # 지금 현재 위치 + K번째까지 확인     
                    nr = r + dr[1]*n
                    nc = c + dc[1]*n
                    # 유효한 위치이면 (arr를 벗어나지 않고, 검은 칸이 아닐 때)
                    if 0 <= nr < N and arr[nr][nc]:
                        white_len += 1
                    # 유효하지 않은 위치이면
                    else:
                        # 지금까지 연속으로 나온 흰색 칸수가 K개인지 확인
                        if white_len == K:          # 딱 K개면
                            perfect_pos_num += 1    # 최종 자리 개수 + 1
                        break
                    
    return perfect_pos_num
    
    
for tc in range(1, 1+int(input())):
    N, K = map(int, input().split())    # N: 퍼즐 크기, K: 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # 퍼즐
    answer = can_words_fit(N, K, arr)
    print(f'#{tc}', answer)