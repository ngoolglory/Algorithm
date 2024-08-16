# 파리 퇴치

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N: 배열 크기, M: 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 배열
    max_kill = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            # 현 위치로부터 오른쪽, 아래, 대각선 아래 합 구하기
            kill = 0  # 현재 위치로부터 파리채 쳤을 때 파리 킬 수 초기값
            for i in range(r, r + M):
                for j in range(c, c + M):
                    kill += arr[i][j]
            # 죽은 파리 개수가 최대값보다 크다면 최대값 갱신
            if kill > max_kill:
                max_kill = kill

    print(f'#{tc}', max_kill)