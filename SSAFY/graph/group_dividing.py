# 그래프_그룹나누기
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def DFS(v):
    global cnt
    for node in adj_l[v]:
        if not visited[node]:
            visited[node] = 1
            DFS(node)


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())    # N: 출석 번호 1~N, M: 신청서 개수
    application = list(map(int, input().split()))
    adj_l = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0

    for i in range(0, M*2, 2):
        n1, n2 = application[i], application[i + 1]
        adj_l[n1].append(n2)
        adj_l[n2].append(n1)
    
    for idx in range(1, N+1):
        if not visited[idx]:
            visited[idx] = 1
            DFS(idx)
            cnt += 1
    
    print(f'#{tc}', cnt)