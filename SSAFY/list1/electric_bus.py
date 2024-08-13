# 배열1_전기버스_확인용

def check_electric_bus(can_move, n_station, n_battery, battery_list):
    pos = 0
    charge_cnt = 0
    while pos < n_station - can_move:
        for i in range(pos + can_move, pos, -1):
            if i in battery_list:
                charge_cnt += 1
                pos = i
                break
        else:
            return 0
    return charge_cnt


if __name__ == "__main__":
    T = int(input())  # 노선 수
    for tc in range(1, T + 1):
        # 한번 충전으로 이동할 수 있는 정류장 개수, 총 정류장 개수, 배터리 설치된 정류장 개수
        can_move, n_station, n_battery = map(int, input().split())
        battery_list = list(map(int, input().split()))  # 배터리 설치된 정류장 번호

        answer = check_electric_bus(can_move, n_station, n_battery, battery_list)
        print(f'#{tc} {answer}')