# 게리맨더링
import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
input = sys.stdin.readline

DEBUG = 1

N = int(input())                                    # 구역의 개수
people = [0] + list(map(int, input().split()))      # 1~N번 구역의 인구
adj_l = [[]]                                        # 인접 리스트
adj_N = [0] * (N+1)                                 # 각 구역의 인접 구역 개수
visited = [0] * (N+1)                               # 방문 리스트
min_diff = 1000

for i in range(1, N+1):
    n, *num = map(int, input().split())
    adj_N[i] = n
    adj_l.append(num)
    
if DEBUG: 
    print('인구 수:', people)
    print('인접 리스트:', adj_l)
    print('구역 별 인접 구역 개수:', adj_N)

def DFS(v, people_sum):
    cnt = 0
    for y in adj_l[x]:
        if not visited[y]:
            cnt += 1
    if cnt == 1:
        
        
    for x in adj_l[v]:
        if not visited[x]:
            DFS(x, people_sum + people[x])
        
    
    
    
for i in range(1, N+1):
    adj_n = adj_N.copy()
    visited = [0] * (N+1)           # 방문 리스트
    visited[i] = 1
    DFS(i, people[i])
    if DEBUG:
        print('시작 노드', i)