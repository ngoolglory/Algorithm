import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

# # 이항 정리
# def comb(n, r):
#     if r == 0 or n == r:
#         return 1
#     if memo[n][r]:          # memo에 0이 아닌 값이 있으면 (이미 답을 구했으면)
#         return memo[n][r]   # 이미 구했던 값 그대로 가져와서 반환
#
#     memo[n][r] = comb(n-1, r-1) + comb(n-1, r)
#     return memo[n][r]
#
# memo = [[0] * 50 for _ in range(50)]    # 메모이제이션을 위한 50*50 배열 초기화
# print(comb(5, 3))

def Pascal(n):
    memo = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or i == j:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
        for x in memo[i]:
            if x:
                print(x, end=' ')
        print()

for tc in range(1, int(input())+1):
    N = int(input())
    print(f'#{tc}')
    Pascal(N)