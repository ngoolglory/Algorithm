# 03_배열2_이웃 원소들의 합

def find_max_of_neighbor_sum(arr_size, arr):
    dr = [1, -1, 0, 0]  # 행 인덱스에 더할 수
    dc = [0, 0, 1, -1]  # 열 인덱스에 더할 수
    max_sum = float('-inf')  # 초기 최대값 무한소로 설정

    for r in range(arr_size):
        for c in range(arr_size):
            temp_sum = arr[r][c]  # 초기 값은 현재 위치
            for k in range(4):  # 상하좌우 인덱스 각각 넣기
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < arr_size and 0 <= nc < arr_size:  # 유효한 인덱스면
                    temp_sum += arr[nr][nc]
            # 현재 위치의 이웃 원소 합이 기존 최대합을 넘으면 최대합 갱신
            if temp_sum > max_sum:
                max_sum = temp_sum

    return max_sum


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        arr_size = int(input())  # 배열의 크기
        arr = [list(map(int, input().split())) for _ in range(arr_size)]
        answer = find_max_of_neighbor_sum(arr_size, arr)
        print(f'#{tc} {answer}')