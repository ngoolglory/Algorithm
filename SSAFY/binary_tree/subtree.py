# 트리_이진탐색_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def dfs(node):
    cnt = 0
    stack = []
    stack.append(node)
    while stack:
        v = stack.pop()
        cnt += 1
        for i in adj_l[v]:
            stack.append(i)
    return cnt

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())            # E: 간선 개수, N: N을 루트로하는 서브트리 구하기 위한 N
    pc_pair = list(map(int, input().split()))   # 부모 자식 쌍
    adj_l = [[] for _ in range(E+1+1)]          # 인접 리스트 (간선 개수 + 1 = 노드 개수)
    
    # 인접 리스트 채우기
    for i in range(0, len(pc_pair), 2):               # 2개씩 부모, 자식 쌍 순회
        parent, child = pc_pair[i], pc_pair[i+1]        # 부모, 자식 쌍
        if child not in adj_l[parent]:                  # 부모 인접 리스트에 해당 자식이 없으면
            adj_l[parent].append(child)                 # 인접 리스트에 추가
    
    answer = dfs(N)
    print(f'#{tc}', answer)