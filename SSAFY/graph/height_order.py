# [Professional] 키 순서 
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def BFS(v, adj_l):
    cnt = 0
    visited = [0] * (N + 1)
    queue = deque([(v)])
    visited[v] = 1
    
    while queue:
        node = queue.popleft()
        for idx in adj_l[node]:
            if not visited[idx]:
                visited[idx] = 1
                cnt += 1
                queue.append(idx)
    
    return cnt


for tc in range(1, 1+int(input())):
    N = int(input())        # N: 학생들의 수
    M = int(input())        # M: 두 학생의 키를 비교한 횟수
    tall_adj = [[] for _ in range(N + 1)]
    short_adj = [[] for _ in range(N + 1)]
    ans = 0

    for _ in range(M):
        a, b = map(int, input().split())
        tall_adj[a].append(b)                      # 인접한 애가 자기보다 더 큰 애
        short_adj[b].append(a)                     # 인접한 애가 자기보다 더 작은 애
    
    for i in range(1, N + 1):
        tall_cnt = BFS(i, tall_adj)
        short_cnt = BFS(i, short_adj)
        if tall_cnt + short_cnt == N - 1:
            ans += 1
    
    print(f'#{tc}', ans)