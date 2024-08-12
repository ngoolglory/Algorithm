# 돌 뒤집기 게임 2
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 돌 개수, M: 뒤집는 횟수
    stones = list(map(int, input().split()))
    
    for _ in range(M):  # M번 뒤집자
        # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 
        # 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둘 거임
        i, j = map(int, input().split())
        i -= 1      # i번째는 인덱스로 하면 i-1   
        
        for k in range(1, j+1):
            left_idx = i - k
            right_idx = i + k
            
            if left_idx < 0 or right_idx >= N:
                break
            
            if stones[left_idx] == stones[right_idx]:       # 같은 색이면
                stones[left_idx] = 1 - stones[left_idx]     # 뒤집어
                stones[right_idx] = 1 - stones[right_idx]   # 뒤집어
            
    print(f'#{tc}', *stones)