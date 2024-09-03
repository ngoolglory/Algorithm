# 탐욕_화물 도크
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())                                        # 신청서 개수
    time_lst = []
    for i in range(N):
        time_lst.append(list(map(int, input().split())))    # 작업 시작 시간, 종료 시간 받기
    
    time_lst.sort(key=lambda x: x[1])                       # 종료 시간이 빠른 순서대로 정렬
    
    end = start = 0
    cnt = 0
    for time in time_lst:
        if time[0] >= end:
            cnt += 1
            end = time[1]
    
    print(f'#{tc}', cnt)