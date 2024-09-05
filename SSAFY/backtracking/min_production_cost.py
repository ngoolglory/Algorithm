# 백트래킹_최소 생산 비용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def backtrack(depth, cost):
    global visited, min_cost
    if cost > min_cost:
        return
    if depth == N:
        if cost < min_cost:
            min_cost = cost
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                backtrack(depth+1, cost+arr[i][depth])
                visited[i] = 0

for tc in range(1, 1+int(input())):
    N = int(input())            # 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]       # N개 제품의 공장별 생산 비용
    visited = [0] * N
    min_cost = 15*99
    backtrack(0, 0)
    print(f'#{tc}', min_cost)