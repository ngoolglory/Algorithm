# [S/W 문제해결 응용] 10일차 - 작업순서
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def BFS():
    order = []
    queue = deque()
    for i in range(1, V+1):
        if not LEVEL[i]:
            queue.append(i)

    while queue:
        v = queue.popleft()
        order.append(v)
        for node in adj_l[v]:
            LEVEL[node] -= 1
            if not LEVEL[node]:
                queue.append(node)

    return order


for tc in range(1, 11):
    V, E = map(int, input().split())
    E_lst = list(map(int, input().split()))
    adj = [[] for _ in range(V+1)]
    adj_l = [[] for _ in range(V+1)]
    LEVEL = [0] * (V + 1)
    
    for i in range(0, E*2, 2):
        n1, n2 = E_lst[i], E_lst[i + 1]
        adj[n1].append(n2)
        adj_l[n2].append(n1)

    for i in range(1, V+1):
        LEVEL[i] = len(adj[i])

    ans = reversed(BFS())
    print(f'#{tc}', *ans)
