# 점점 커지는 당근의 개수
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())    # 당근 개수
    arr = list(map(int, input().split()))   # 당근 크기 배열
    
    max_continue = 1        # 연속으로 커진 최대 개수 (한번도 안커졌을 경우를 대비해 초기값은 1)
    cur_continue = 1        # 현재 연속 커진 개수
    
    for i in range(1, N):
        if arr[i-1] < arr[i]:       # 이전 당근보다 현재 당근이 더 크면
            cur_continue += 1
        else:                       # 커지지 않은 경우
            cur_continue = 1        # 현재 연속 커진 개수 1로 초기화
        if max_continue < cur_continue:     # 기존 최대 개수보다 크면 
            max_continue = cur_continue     # 최대값 갱신
        
    print(f'#{tc}', max_continue)