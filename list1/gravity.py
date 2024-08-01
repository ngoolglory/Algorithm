# 배열1_gravity

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    h_list = list(map(int, input().split()))
    max_fall = 0  # 최대 낙하 거리

    for i in range(N - 1):  # 맨 아래 층을 제외한 모든 층 순회
        below_block = 0  # i번째 층 가장 위 블럭 아래 깔리는 블럭의 수
        for j in range(i + 1, N):  # i번째 층부터 마지막 층까지 순회
            if h_list[i] <= h_list[j]:  # 중력 작용 시 현재 블럭 아래 깔릴 블럭이면
                below_block += 1

        current_fall = (N - i) - below_block - 1  # 현재 블럭 낙하 거리
        # 최대 낙하 거리보다 현재 블럭 낙하 거리가 더 크면 최대 낙하 거리 갱신
        if max_fall < current_fall:
            max_fall = current_fall

        # 남은 층보다 max_fall이 더 크면 반복 종료
        if max_fall > N - i:
            break

    print(f'#{tc} {max_fall}')