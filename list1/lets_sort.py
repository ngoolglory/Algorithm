# 숫자를 정렬하자

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    print(f'#{tc}', end=' ')

    for end_point in range(N - 1, 0, -1):
        swap_flag = False
        for i in range(end_point):
            if num_list[i] > num_list[i + 1]:
                swap_flag = True
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        if swap_flag == False:
            break

    for element in num_list:
        print(element, end=' ')
    print()