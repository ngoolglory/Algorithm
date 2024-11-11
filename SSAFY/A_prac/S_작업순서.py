# [S/W 문제해결 응용] 10일차 - 작업순서
import sys
from collections import deque
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

T = 10
for tc in range(1, 1+T):
    V, E = map(int, input().split())          # V: 정점 개수, E: 간선 개수
    edges = list(map(int, input().split()))   # 간선 정보
    
    # 인접 리스트, indegree(다른 노드로부터 들어오는 간선 개수) 배열 생성
    adj_l = [[] for _ in range(V+1)]
    indegree = [0] * (V+1)
    
    # 간선 정보 입력
    for i in range(E):
        start = edges[2 * i]
        end = edges[2 * i + 1]
        adj_l[start].append(end)
        indegree[end] += 1
    
    # 진입 차수가 0인 노드를 큐에 넣기 (들어오는 간선이 없는 조상 노드들)
    queue = deque([i for i in range(1, V+1) if indegree[i] == 0])
    result = []
    
    # 위상 정렬 수행
    while queue:
        node = queue.popleft()
        result.append(node)
    
        # 현재 노드의 자식들 진입 차수를 1 감소시키고 0이 되면 큐에 추가    
        for child in adj_l[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    
    # 결과 출력
    print(f'#{tc}', ' '.join(map(str, result)))