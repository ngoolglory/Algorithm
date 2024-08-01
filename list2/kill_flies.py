# 파리 퇴치

def kill_flies(arr_size, kill_size, arr):
    max_kill_cnt = 0  # 죽인 파리 최대 수

    for r in range(arr_size):
        for c in range(arr_size):
            kill_sum = 0  # 죽인 파리 수
            # 파리채 영역 만큼 파리 잡기
            for kill_r in range(r, r + kill_size):
                for kill_c in range(c, c + kill_size):
                    # 유효한 인덱스면
                    if 0 <= kill_r < arr_size and 0 <= kill_c < arr_size:
                        kill_sum += arr[kill_r][kill_c]

            if kill_sum > max_kill_cnt:  # 죽인 파리 수가 최대값보다 크면
                max_kill_cnt = kill_sum  # 최대값 갱신

    return max_kill_cnt


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        arr_size, kill_size = map(int, input().split())  # 배열의 크기, 파리채 크기
        arr = [list(map(int, input().split())) for _ in range(arr_size)]  # 배열
        answer = kill_flies(arr_size, kill_size, arr)
        print(f'#{tc} {answer}')