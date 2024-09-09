# 두 전구
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

result_list = []
for tc in range(1, int(input())+1):
    A, B, C, D = map(int, input().split())
    
    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)

    result = end - start
    if result <= 0:     # 안 겹치는 경우
        result = 0
    
    result_list.append(result)

for idx, result in enumerate(result_list):
    print(f'#{idx + 1}', result)