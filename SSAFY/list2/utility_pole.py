# 전봇대
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    N = int(input())
    pos_lst = []
    for _ in range(N):
        start, end = map(int, input().split())
        pos_lst.append([start, end])
    
    pos_lst.sort(reverse=True)

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if pos_lst[i][1] < pos_lst[j][1]:
                cnt += 1

    print(f'#{tc}', cnt)