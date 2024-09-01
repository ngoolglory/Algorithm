# [S/W 문제해결 기본] 9일차 - 사칙연산
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def DFS(v):
    if tree[v] not in list('+-*/'):
        return tree[v]
    left_v = DFS(left[v])
    right_v = DFS(right[v])
    if tree[v] == '+':
        return left_v + right_v
    elif tree[v] == '-':
        return left_v - right_v
    elif tree[v] == '*':
        return left_v * right_v
    else:
        return left_v / right_v


for tc in range(1, 11):
    N = int(input())        # 노드 개수
    left = [0] * (N+1)      # 왼쪽 자식 노드
    right = [0] * (N+1)     # 오른쪽 자식 노드
    tree = [0] * (N+1)      # 노드에 들어가 있는 값

    for _ in range(N):
        node, value, *children = input().split()
        node, children = int(node), list(map(int, children))
        if children:
            left[node] = children[0]
            if len(children) == 2:
                right[node]= children[1]
        else:
            value = int(value)
        tree[node] = value
    print(f'#{tc}', int(DFS(1)))