# 달팽이 숫자

def snail_number(arr_size):
    arr = [[0]*arr_size for _ in range(arr_size)]  # 배열 생성
    direction_list = ['right', 'down', 'left', 'up']    # 우 -> 하 -> 좌 -> 상 순으로 방향 변경
    direction_idx = 0
    r, c = 0, -1  # 현재 행과 열 좌표 초기화 (오른쪽으로 이동할 때 c += 1이므로 c를 -1로 시작)
    num = 1  # 현재 번호

    while num <= arr_size ** 2:  # num이 전체 칸 수보다 커지면 반복문 종료
        # 현재 방향에 따라 위치 이동
        if direction_list[direction_idx] == 'right':
            c += 1
        elif direction_list[direction_idx] == 'down':
            r += 1
        elif direction_list[direction_idx] == 'left':
            c -= 1
        elif direction_list[direction_idx] == 'up':
            r -= 1

        # 벽이나 이미 숫자가 있는지 확인
        if 0 <= r < arr_size and 0 <= c < arr_size and not arr[r][c]:
            arr[r][c] = num
            num += 1
        else:  # 벽이거나 이미 숫자가 있으면
            # 다시 이전 위치로 돌아가기
            if direction_list[direction_idx] == 'right':
                c -= 1
            elif direction_list[direction_idx] == 'down':
                r -= 1
            elif direction_list[direction_idx] == 'left':
                c += 1
            elif direction_list[direction_idx] == 'up':
                r += 1
            # 방향 전환
            direction_idx = (direction_idx + 1) % 4

    # 최종 배열 출력
    for inner_list in arr:
        print(*inner_list)


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        arr_size = int(input())
        print(f'#{tc}')  # 테스트 케이스 번호 출력
        snail_number(arr_size)  # 달팽이 출력