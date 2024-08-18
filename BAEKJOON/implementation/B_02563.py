# 색종이
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

N = int(input())                                # 색종이의 수
visited = [[0] * 100 for _ in range(100)]       # 방문 리스트
area = 0
for _ in range(N):
    nc, nr = map(int, input().split())          # 색종이 좌측 하단 좌표
    for r in range(nr, nr+10):
        for c in range(nc, nc+10):
            if not visited[r][c]:
                visited[r][c] = 1
                area += 1
print(area)