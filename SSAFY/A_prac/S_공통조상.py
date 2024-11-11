# [S/W 문제해결 응용] 3일차 - 공통조상
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

'''
한번의 DFS로 아래 정보 다 얻을 수 있음
1. 각 노드의 부모 노드 번호
2. 각 노드의 깊이
3. 각 노드마다 이 노드가 루트인 서브트리의 크기
'''

def dfs(cur, prv):
    global par, depth, sz
    sz[cur] = 1
    par[cur] = prv
    for nxt in adj_l[cur]:
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)
        sz[cur] += sz[nxt]

def find_lca(n1, n2):
    # 두 노드의 깊이를 맞추기 (같은 깊이가 될 때까지 올라가)
    while depth[n1] > depth[n2]:
        n1 = par[n1]
    while depth[n2] > depth[n1]:
        n2 = par[n2]
    # 공통 조상 찾기
    while n1 != n2:
        n1 = par[n1]
        n2 = par[n2]
    return n1


T = int(input())
for tc in range(1, T+1):
    # 정점 개수 V, 간선 개수 E, 정점1 n1, 정점2 n2
    V, E, n1, n2 = map(int, input().split())
    edges = list(map(int, input().split()))     # 간선 정보
    
    # 인접리스트 만들기
    adj_l = [[] for _ in range(V+1)]
    
    # 인접리스트 채우기
    for i in range(E):
        start = edges[2 * i]
        end = edges[2 * i + 1]
        adj_l[start].append(end)
    
    # 부모, 깊이, 서브트리 크기 배열 초기화
    par = [0] * (V+1)
    depth = [0] * (V+1)
    sz = [0] * (V+1)
    
    # DFS로 각 노드의 부모, 깊이, 서브트리 크기 계산
    dfs(1, 1)
    
    # 가장 가까운 공통 조상 찾기
    lca = find_lca(n1, n2)
    
    # 출력
    print(f'#{tc} {lca} {sz[lca]}')