# [S/W 문제해결 기본] 2일차 - Sum

def sum_func(arr):
    max_v = float('-inf')  # 최댓값 초기값으로 -무한대 설정

    diag_left_sum = 0  # 좌하향 대각선의 합
    diag_right_sum = 0  # 우하향 대각선의 합

    # 행의 합
    for i in range(100):
        row_sum = 0  # 행의 합
        col_sum = 0  # 열의 합

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
            if i == j:  # 좌하향 대각선 원소이면
                diag_left_sum += arr[i][j]
            if i == 99 - j:  # 우하향 대각선 원소이면
                diag_right_sum += arr[i][j]

        if row_sum > max_v:  # 최댓값보다 이번 행의 합이 더 크면
            max_v = row_sum  # 최댓값 갱신
        if col_sum > max_v:  # 최댓값보다 이번 열의 합이 더 크면
            max_v = col_sum  # 최댓값 갱신
    if diag_left_sum > max_v:  # 최댓값보다 좌하향 대각선 원소 합이 더 크면
        max_v = diag_left_sum  # 최댓값 갱신
    if diag_right_sum > max_v:  # 최댓값보다 우하향 대각선 원소 합이 더 크면
        max_v = diag_right_sum  # 최댓값 갱신

    return max_v


if __name__ == "__main__":
    for _ in range(10):  # 10개의 test cases
        tc = int(input())  # test case 번호
        arr = [list(map(int, input().split())) for _ in range(100)]  # 2차원 배열
        answer = sum_func(arr)
        print(f'#{tc} {answer}')