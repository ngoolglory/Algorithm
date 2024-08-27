# 트리_subtree_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def dfs(node):
    cnt = 0                     # 카운트 초기화
    stack = []                  # 빈 스택 생성
    stack.append(node)          # 시작 루트 노드 stack에 넣고 시작
    while stack:                # 스택에 아무것도 남지 않을 때까지 반복
        v = stack.pop()         # 스택 top 원소 pop
        cnt += 1                # pop할 때마다 카운트 1증가
        for i in adj_l[v]:      # pop한 노드의 인접 노드 모두 스택에 넣기
            stack.append(i)
    return cnt                  # 최종 카운트 반환

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