# 오목
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
<나올 수 있는 결과>
1. 검은색 win (1)
2. 흰색 win (2)
3. 아직 승부나지 X (0)

정확히 5개가 연속으로 있어야 이긴 것. (6개 연속은 이긴 거 아님)
'''

def omok(arr):
    stone = -1                   # 돌 종류
    # → ↓ ↘ ↗ (왜? 가장 왼쪽에 있는 바둑알의 좌표를 출력해야 하니까!!)
    dr = [0, 1, 1, -1]           # 행 델타
    dc = [1, 0, 1, 1]            # 열 델타
    
    for r in range(19):
        for c in range(19):
            
            if arr[r][c] == 0: continue       # 돌 없는 경우 패스
            stone = arr[r][c]                 # 현재 돌의 종류             

            for k in range(4):                # 우, 우하, 하, 좌하 탐색
                cnt = 1                       # 돌 하나는 찾은 상태니 초기값 1
                for n in range(1, 6):         # 6목 여부도 봐야하니 6까지
                    nr = r + dr[k]*n
                    nc = c + dc[k]*n
                    if 0 <= nr < 19 and 0 <= nc < 19 and arr[nr][nc] == stone:
                        cnt += 1
                    else:
                        break
                if cnt == 5:                  # 정확히 5개 연속일 때만
                    # 이전 위치에 같은 돌이 있는지 확인
                    prev_r = r - dr[k]
                    prev_c = c - dc[k]
                    if 0 <= prev_r < 19 and 0 <= prev_c < 19 and arr[prev_r][prev_c] == stone:
                        continue
                    # 이전 위치에 같은 돌이 없으면 정확히 5개 연속이라는 뜻이므로
                    return stone, (r+1, c+1)  # 해당 돌 승리 (with 가장 왼쪽 돌 좌표)
    return 0, None                            # 마지막까지 승리자 없으면 0 반환

arr = [list(map(int, input().split())) for _ in range(19)]  # 바둑판
winner, pos = omok(arr)
print(winner)
if winner:      # 승부가 결정난 경우만 출력
    print(*pos)