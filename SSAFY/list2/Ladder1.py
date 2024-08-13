# [S/W 문제해결 기본] 2일차 - Ladder1

def find_X_in_ladder(arr):
    # 제일 마지막 줄 도착 위치 컬럼 찾기
    for i in range(len(arr[-1])):
        if arr[-1][i] == 2:
            break
    # 도착지점(X) 좌표
    cur_r, cur_c = len(arr)-1, i

    # X부터 시작지점까지 찾아 올라가기
    while True:
        # 끝에 도달했으면 좌표 리턴
        if arr[cur_r-1][cur_c] == -1:
            return cur_c - 1  # 0번 인덱스가 패딩이므로 -1 해야 정확한 위치가 나옴
        # 오른쪽만 길이 있으면 오른쪽으로 끝까지 이동
        if arr[cur_r][cur_c+1] == 1:
            while arr[cur_r][cur_c+1] != 0:
                cur_c += 1
                arr[cur_r][cur_c] = 0  # 지나온 위치를 0으로 바꿔서 벽으로 만듦
        # 왼쪽만 길이 있으면 왼쪽으로 끝까지 이동
        elif arr[cur_r][cur_c-1] == 1:
            while arr[cur_r][cur_c-1] != 0:
                cur_c -= 1
                arr[cur_r][cur_c] = 0  # 지나온 위치를 0으로 바꿔서 벽으로 만듦
        # 양옆에 길이 없으면 위로 올라가기
        else:
            cur_r -= 1


if __name__ == "__main__":
    for _ in range(10):
        tc = int(input())
        # 가장 윗 줄은 -1로 채우고 양 옆은 0으로 패딩 (102*101 크기)
        arr = [[-1 for _ in range(102)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
        answer = find_X_in_ladder(arr)
        print(f'#{tc}', answer)