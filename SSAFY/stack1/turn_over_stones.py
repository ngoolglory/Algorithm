import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())            # N: 돌 개수, M: 뒤집기 횟수
    stones = [0] + list(map(int, input().split()))    # 돌 상태
    for _ in range(M):
        i, j = map(int, input().split())        # i번째부터 j개 뒤집기
        if i+j >= len(stones):          # 뒤집을 돌 번호가 리스트 인덱스를 넘어가면
            j = len(stones) - i         # j를 마지막 칸에 맞추기
        for idx in range(i, i+j):
            stones[idx] = stones[i]

    print(f'#{tc}', *stones[1:])