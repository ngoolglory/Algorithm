# 배열1_구간합_확인용

T = int(input())  # 테스트케이스의 개수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 정수의 개수, M: 구간의 개수
    num_list = list(map(int, input().split()))  # 숫자 리스트

    count = 0
    min_prefix_sum = float('inf')
    max_prefix_sum = float('-inf')
    while True:
        try:
            prefix_sum = 0
            for i in range(M):  # M개만큼 구간 합
                prefix_sum += num_list[count + i]
            if prefix_sum < min_prefix_sum:
                min_prefix_sum = prefix_sum
            if prefix_sum > max_prefix_sum:
                max_prefix_sum = prefix_sum
            count += 1
        except IndexError:
            break

    print(f'#{tc} {max_prefix_sum - min_prefix_sum}')