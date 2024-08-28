# 트리_노드의합_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def post_order(node):         
    if node > N:                        # 노드 번호가 트리의 노드 개수를 넘어버리면
        return 0                        # 0 반환 (어차피 0은 더해도 똑같으니까 그냥 더미 역할)
    if tree[node] > 0:                  # 이미 값이 저장된 노드라면 그대로 반환
        return tree[node]
            
    # 현재 노드에 왼쪽과 오른쪽 자식 노드 값의 합을 저장
    tree[node] = post_order(node * 2) + post_order(node * 2 + 1)
    return tree[node]                   # 현재 노드 값을 반환


for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())                # N: 노드 개수, M: 리프 노드 개수, L: 값을 출력할 노드 번호
    tree = [0] * (N + 1)                               # 트리 초기화
    for _ in range(M):
        node, value = map(int, input().split())        # 리프 노드, 값 쌍 받기
        tree[node] = value                             # 트리에 리프 노드 값 저장
    post_order(1)                                      # 루트 노드부터 후위 순회 시작       
    print(f'#{tc}', tree[L])