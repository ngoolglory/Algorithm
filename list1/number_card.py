# 배열1_숫자카드_확인용

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # N: 카드 장수
    num_list = list(map(int, list(input())))
    counts = [0 for _ in range(10)]

    for num in num_list:
        counts[num] += 1

    max_idx = 0
    for i in range(1, len(counts)):
        if counts[max_idx] <= counts[i]:
            max_idx = i

    print(f'#{tc} {max_idx} {counts[max_idx]}')