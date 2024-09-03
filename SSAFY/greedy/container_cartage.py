# 탐욕_컨테이너 운반
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())                                  # N: 컨테이너의 수, M: 트럭 수
    w_lst = sorted(list(map(int, input().split())), reverse=True)     # 내림차순 정렬된 N개 화물의 무게 리스트
    t_lst = sorted(list(map(int, input().split())), reverse=True)     # 내림차순 정렬된 M개 트럭의 적재 용량 리스트
    
    total_w = 0
    for i in range(len(t_lst)):
        for j in range(i, len(w_lst)):
            if t_lst[i] - w_lst[j] >= 0:
                total_w += w_lst[j]
                break
        if i == 0 and total_w == 0:
            break

    print(f'#{tc}', total_w)