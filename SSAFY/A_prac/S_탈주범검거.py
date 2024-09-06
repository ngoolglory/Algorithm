# [모의 SW 역량테스트] 탈주범 검거
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    move = [[(1,0),(-1,0),(0,1),(0,-1)],
            [(1,0),(-1,0)],
            [(0,1),(0,-1)],
            [(-1,0),(0,1)],
            [(1,0),(0,1)],
            [(0,-1),(1,0)],
            [(-1,0),(0,-1)]]