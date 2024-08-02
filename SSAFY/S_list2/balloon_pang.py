def balloon_pang(N, M, arr):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    max_flowers = 0
    for r in range(N):
        for c in range(M):
            flowers = arr[r][c]
            for i in range(4):
                if 0 <= r + dr[i] < N and 0 <= c + dc[i] < M:
                    flowers += arr[r + dr[i]][c + dc[i]]
            if flowers > max_flowers:
                max_flowers = flowers
    return max_flowers

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = balloon_pang(N, M, arr)
    print(f'#{tc}', answer)