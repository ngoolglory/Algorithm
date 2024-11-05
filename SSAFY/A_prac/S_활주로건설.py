# [모의 SW 역량테스트] 활주로 건설
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")


T = int(input())
for tc in range(1, 1+T):
    N, X = map(int, input().split())    # N: 맵 크기, X: 활주로 길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # 맵
    CNT = 0     # 활주로를 건설할 수 있는 경우의 수 (정답 변수)
    
    
    # 세로로 읽기
    for c in range(N):
        prev = arr[0][c]        # 이전 위치의 높이
        conti = 1               # 동일 높이 연속으로 나온 횟수
        visited = [0] * N       # 방문 리스트 (이미 건설된 곳에 또 건설하는 것 막기 위함)
        for r in range(1, N):
            # 이미 건설된 곳이면 넘어가
            if visited[r]:
                continue
            
            cur = arr[r][c]     # 현재 위치의 높이
            conti += 1
            
            # 순서대로 읽다가 높이가 한번에 2 이상 차이나면 그 줄은 제외
            if abs(cur - prev) >= 2:
                break
            
            # 한 칸 내려갔으면 지금부터 동일 높이 연속 X개 여부 확인
            if cur - prev == -1:
                break_flag = False
                for k in range(X):
                    nr = r + k
                    # 배열을 벗어나지 않으면서 동일 높이가 연속으로 나오면
                    if nr < N and cur == arr[nr][c]:
                        visited[nr] = 1     # 방문 처리
                    # 배열 벗어나거나 높이가 바뀌면 break
                    else:
                        break_flag = True
                if break_flag:
                    break
                conti = 0       # 동일 높이 연속 횟수 초기화
            
            # 한 칸 올라갔으면 지금까지 동일 높이 연속 X개 여부 확인
            elif cur - prev == 1:
                conti -= 1
                if conti < X:
                    break
                conti = 1       # 동일 높이 연속 횟수 초기화
            
            prev = cur
        
        # for-else문: 한번도 break에 걸리지 않았다면
        else:
            CNT += 1

    
    # 가로로 읽기
    for r in range(N):
        prev = arr[r][0]        # 이전 위치의 높이
        conti = 1               # 동일 높이 연속으로 나온 횟수
        visited = [0] * N       # 방문 리스트 (이미 건설된 곳에 또 건설하는 것 막기 위함)
        for c in range(1, N):
            # 이미 건설된 곳이면 넘어가
            if visited[c]:
                continue
            
            cur = arr[r][c]     # 현재 위치의 높이
            conti += 1
            
            # 순서대로 읽다가 높이가 한번에 2 이상 차이나면 그 줄은 제외
            if abs(cur - prev) >= 2:
                break
            
            # 한 칸 내려갔으면 지금부터 동일 높이 연속 X개 여부 확인
            if cur - prev == -1:
                break_flag = False
                for k in range(X):
                    nc = c + k
                    # 배열을 벗어나지 않으면서 동일 높이가 연속으로 나오면
                    if nc < N and cur == arr[r][nc]:
                        visited[nc] = 1     # 방문 처리
                    # 배열 벗어나거나 높이가 바뀌면 break
                    else:
                        break_flag = True
                if break_flag:
                    break
                conti = 0       # 동일 높이 연속 횟수 초기화
            
            # 한 칸 올라갔으면 지금까지 동일 높이 연속 X개 여부 확인
            elif cur - prev == 1:
                conti -= 1
                if conti < X:
                    break
                conti = 1       # 동일 높이 연속 횟수 초기화
            
            prev = cur
        
        # for-else문: 한번도 break에 걸리지 않았다면
        else:
            CNT += 1
     
            
    print(f'#{tc} {CNT}')