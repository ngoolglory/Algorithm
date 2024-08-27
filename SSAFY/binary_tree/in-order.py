# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def in_order(node):                 # 중위 순회
    if node:                        # 자식 노드가 존재하지 않으면 종료
        in_order(left[node])        # 현재 노드 기준 왼쪽 노드 재귀
        print(tree[node], end='')   # 왼쪽 끝 노드까지 갔으면 현재 카운트 집어넣고 
        in_order(right[node])       # 현재 노드 기준 오른쪽 노드 재귀


for tc in range(1, 11):
    N = int(input())                # 트리의 노드 수
    left = [0]*(N+1)                # 부모를 인덱스로 왼쪽 자식 번호 저장
    right = [0]*(N+1)               # 부모를 인덱스로 오른쪽 자식 번호 저장
    tree = [0]*(N+1)                # 트리 배열

    # 트리, 자식 배열 채우기
    for _ in range(N):
        node, value, *children = input().split()
        node, children = int(node), list(map(int, children))
        tree[node] = value
        if children:                        # 자식이 존재하면
            left[node] = children[0]        # 일단 왼쪽 자식부터 넣고
            if len(children) == 2:          # 자식 노드가 두개면
                right[node] = children[1]   # 오른쪽 자식도 추가

    print(f'#{tc}', end=' ')
    in_order(1)
    print()