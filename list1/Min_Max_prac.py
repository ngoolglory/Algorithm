# 배열1_Min_Max_확인용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    min_val = float("inf")
    max_val = float("-inf")
    for num in num_list:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print(f'#{tc} {max_val-min_val}')