# [S/W 문제해결 기본] 1일차 - Flatten

for tc in range(1, 11):
    dump_num = int(input())
    h_list = list(map(int, input().split()))

    for _ in range(dump_num):  # dump 횟수만큼 순회
        # 현재 최소, 최대 높이 구하기
        min_idx = 0
        max_idx = 0
        for i in range(len(h_list)):
            if h_list[i] < h_list[min_idx]:
                min_idx = i
            if h_list[i] > h_list[max_idx]:
                max_idx = i

        # 박스 옮기기
        h_list[max_idx] -= 1
        h_list[min_idx] += 1

        # 최소, 최대 차이 구하기
        diff = h_list[max_idx] - h_list[min_idx]
        if diff <= 1:
            break

    # 현재 최소, 최대 높이 구하기
    min_idx = 0
    max_idx = 0
    for i in range(len(h_list)):
        if h_list[i] < h_list[min_idx]:
            min_idx = i
        if h_list[i] > h_list[max_idx]:
            max_idx = i

    # 최소, 최대 차이 구하기
    diff = h_list[max_idx] - h_list[min_idx]

    print(f'#{tc} {diff}')