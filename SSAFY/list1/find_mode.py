# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())  # 테스트케이스 수

for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    counts = [0] * 101

    for score in scores:
        counts[score] += 1

    max_freq_idx = 0
    for i in range(len(counts)):
        if counts[i] >= counts[max_freq_idx]:
            max_freq_idx = i

    print(f'#{tc} {max_freq_idx}')