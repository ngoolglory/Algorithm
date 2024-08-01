# 03_배열1_이웃원소의합

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 정수값의 개수
    num_list = list(map(int, input().split()))  # 정수값 리스트

    prefix_sum_max = num_list[0] + num_list[1]
    for i in range(1, N - 1):
        prefix_sum = num_list[i] + num_list[i + 1]
        if prefix_sum > prefix_sum_max:
            prefix_sum_max = prefix_sum

    print(f'#{tc} {prefix_sum_max}')