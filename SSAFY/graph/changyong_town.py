# 창용 마을 무리의 개수
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def DFS(v):
    for i in adj_l[v]:
        if not visited[i]:
            visited[i] = 1
            DFS(i)


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 창용 마을에 사는 사람 수, M: 서로를 알고 있는 사람의 관계 수
    adj_l = [[] for _ in range(N+1)]
    visited = [0] * (N + 1)
    
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj_l[n1].append(n2)
        adj_l[n2].append(n1)

    cnt = 0
    for idx in range(1, N+1):
        if not visited[idx]:
            visited[idx] = 1
            DFS(idx)
            cnt += 1

    print(f'#{tc}', cnt)