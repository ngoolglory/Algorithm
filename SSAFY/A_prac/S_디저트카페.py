# [모의 SW 역량테스트] 디저트 카페
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

'''
시작 불가 위치 : (0, 0), (0, N-1), (N-1, 0), (N-1, N-1)
우하 : (1, 1)
좌하 : (1, -1)
좌상 : (-1, -1)
우상 : (-1, 1)
'''

DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def DFS():
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    