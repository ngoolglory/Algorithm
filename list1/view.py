# View

for tc in range(1, 11):
    N = int(input())  # N: 건물의 개수
    height_list = list(map(int, input().split()))  # 각 건물의 높이 리스트
    total = 0  # 조망권 확보된 총 세대 수

    for i in range(2, N - 2):  # 양 옆 2칸의 건물 높이는 항상 0이므로 2~N-2 순회
        surround_max = float("-inf")  # 주변 건물의 최대값 초기값 설정
        for j in [-2, -1, 1, 2]:  # 양쪽 각각 건물 2개의 인덱스
            if height_list[i] <= height_list[i + j]:  # 주변에 현재 건물보다 높거나 높이가 같은 건물이 있으면 주변 탐색 종료
                break
            elif height_list[i + j] > surround_max:  # 주변 건물이 최대값보다 높을 때
                surround_max = height_list[i + j]  # 최대값 갱신
        else:  # 주변 모든 건물이 현 건물보다 낮으면
            total += height_list[i] - surround_max  # 조망권 확보된 세대 수 구해서 총 세대 수에 더하기

    print(f'#{tc} {total}')  # 조망권 확보된 세대의 수