# 돌 뒤집기 게임 1
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 돌 개수, M: 뒤집는 횟수
    stones = list(map(int, input().split()))
    
    for _ in range(M):  # M번 뒤집자
        # i번째부터 j개 돌을 i번째 돌 색으로 바꿔놓을 거임
        i, j = map(int, input().split())    
        for idx in range(i-1, i-1+j):
            # try except 이용해서 만약 인덱스 넘어가면 for문 break
            try:
                stones[idx] = stones[i-1]   # i번째 돌 색으로 바꿔
            except:
                break
            
    print(f'#{tc}', *stones)