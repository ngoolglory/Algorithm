# 03_배열2_농작물 수확
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    N = int(input())    # 농장 크기
    farm = [list(map(int, input().split())) for _ in range(N)]      # 농장
    min_diff = float('inf')     # 차이의 최소값
    final_min_cost = 0          # 최종 농지를 만들기 위한 최소 비용

    # 경계선의 교점: r, c
    # area1: 행(0 ~ r-1), 열(0 ~ c-1)
    # area2: 행(r ~ N-1), 열(0 ~ c-1)
    # area3: 행(0 ~ N-1), 열(c ~ N-1)
    # 사각영역의 가로와 세로의 크기는 최소 1이상이어야 하므로 경계는 무조건 (1,1)부터 시작
    for r in range(1, N):
        for c in range(1, N):

            # 1, 2, 3번 영역 농작물 합 초기화
            area1 = area2 = area3 = 0

            # area1 농작물 합
            for i in range(r):
                for j in range(c):
                    area1 += farm[i][j]

            # area2 농작물 합
            for i in range(r, N):
                for j in range(c):
                    area2 += farm[i][j]

            # area3 농작물 합
            for i in range(N):
                for j in range(c, N):
                    area3 += farm[i][j]

            # 최대값, 최소값 차이
            max_cost = max([area1, area2, area3])
            min_cost = min([area1, area2, area3])
            diff = max_cost - min_cost

            # 차이가 최소값보다 작으면 최소값 갱신
            if diff < min_diff:
                min_diff = diff

    print(f'#{tc}', min_diff)