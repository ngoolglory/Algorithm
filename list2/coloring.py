# 배열2_색칠하기_확인용

def coloring(n_box, boxes_info):
    grid = [[0] * 10 for _ in range(10)]
    # 빨간 박스 영역 색칠하기
    for box_info in boxes_info:
        r1, c1, r2, c2, color = box_info
        for i in range(r1, r2 + 1):  # r1 ~ r2
            for j in range(c1, c2 + 1):  # c1 ~ c2
                if grid[i][j] == 0:  # 칠해져 있지 않으면
                    grid[i][j] = color  # 해당 색깔로 색칠
                elif grid[i][j] != color:  # 다른 색깔이 칠해져 있으면
                    grid[i][j] = 3  # 보라색(3)으로 변경

    # 빨강, 파랑 겹친 영역은 두번 색칠되었으니 2임
    area = 0  # 보라색 칸수
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:  # 보라색이면
                area += 1

    return area


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        n_box = int(input())
        boxes_info = []
        for _ in range(n_box):  # 0 ~ n_box-1
            boxes_info.append(list(map(int, input().split())))  # 각 박스 정보를 boxes_info 리스트에 담기
        answer = coloring(n_box, boxes_info)
        print(f'#{tc} {answer}')