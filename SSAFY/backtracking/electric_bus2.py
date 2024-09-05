# 백트래킹_전기버스2
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def backtrack(pos, power, cnt):
    global min_cnt
    if cnt > min_cnt:
        return
    if pos == N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    else:
        for i in range(power, 0, -1):
            if pos + i <= N-1:
                backtrack(pos+i, arr[pos+i], cnt+1)

for tc in range(1, 1+int(input())):
    N, *arr = list(map(int, input().split()))
    arr += [0]
    min_cnt = N - 2
    backtrack(0, arr[0], 0)
    print(f'#{tc}', min_cnt-1)      # 첫 위치에서 이동하는 경우는 교환 횟수에 포함되지 않음