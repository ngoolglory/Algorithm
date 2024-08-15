# 의석이의 세로로 말해요
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
    arr = []                # 칠판
    for _ in range(5):      # 항상 5줄만 주어짐
        words = list(input())       # 한 줄 글자들 받기
        words += [-1] * (15 - len(words))   # 길이는 15개로 맞춰줌
        arr.append(words)
    
    print(f'#{tc}', end=' ')
    for c in range(15):
        for r in range(5):
            if arr[r][c] == -1:     # -1이면 출력X
                continue
            else:                   # -1 아니면 출력
                print(arr[r][c], end='')
    
    print()     # 다음 테스트케이스를 위한 줄바꿈