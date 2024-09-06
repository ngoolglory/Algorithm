# 장훈이의 높은 선반
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def backtrack(depth, sum_h):
    global min_sum

    if sum_h >= B:
        min_sum = min(min_sum, sum_h)
        return

    if depth == N:
        return

    if sum_h >= min_sum:
        return

    backtrack(depth + 1, sum_h + H[depth])
    backtrack(depth + 1, sum_h)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())                # N: 점원 수, B: 선반 높이
    H = list(map(int, input().split()))             # 점원들 키
    min_sum = 10000 * N

    backtrack(0, 0)
    
    print(f'#{tc}', min_sum - B)