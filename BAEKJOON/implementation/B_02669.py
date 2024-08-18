# 직사각형 네개의 합집합의 면적 구하기
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
입력은 4줄이고, 하나의 입력은 아래 4가지 정보 제공
입력: 왼쪽 아래 꼭짓점 x, y 좌표, 오른쪽 위 꼭짓점의 x, y 좌표
좌표 평면 범위: 1 ~ 100
'''

visited = [[0]*101 for _ in range(101)]     # 방문 배열
cnt = 0                                     # 면적 내 사각형 개수
for _ in range(4):                          # 입력은 4줄
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            if not visited[r][c]:           # 방문한적 없으면
                visited[r][c] = 1           # 방문 표시
                cnt += 1                    # 사각형 1개 카운트
print(cnt)