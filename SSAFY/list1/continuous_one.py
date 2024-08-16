# 연속한 1의 개수
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())    # 수열의 길이
    arr = list(map(int, list(input()))) + [0]    # 수열
    cnt = 0             # 연속으로 나온 1의 개수
    max_cnt = 0         # 연속으로 나온 1의 개수의 최대값

    for num in arr:
        if num == 1:            # 1 나오면
            cnt += 1            # 카운트 1 증가
        else:                   # 0 나오면
            if cnt > max_cnt:   # 지금까지 카운트가 최대값보다 크면
                max_cnt = cnt   # 최대 카운트 갱신
            cnt = 0

    print(f'#{tc}', max_cnt)