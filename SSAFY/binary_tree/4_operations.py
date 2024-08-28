# [S/W 문제해결 기본] 9일차 - 사칙연산
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def calculator(v):
    global tree
    if tree[v] not in ['+','-','*','/']:
        return tree[v]
    else:
        left_v = calculator(left[v])
        right_v = calculator(right[v])
        if tree[v] == '+':
            tree[v] = left_v + right_v
        elif tree[v] == '-':
            tree[v] = left_v - right_v
        elif tree[v] == '*':
            tree[v] = left_v * right_v
        else:
            tree[v] = left_v / right_v
        return tree[v]


for tc in range(1, 11):
    N = int(input())        # 노드 개수
    left = [0] * (N+1)      # 왼쪽 자식 노드
    right = [0] * (N+1)     # 오른쪽 자식 노드
    tree = [0] * (N+1)      # 노드에 들어가 있는 값

    for _ in range(N):
        node, value, *children = list(input().split())
        node, children = int(node), list(map(int, children))
        if value not in ['+','-','*','/']:
            tree[node] = int(value)
        else:
            tree[node] = value
        if children:
            left[node] = children[0]
            if len(children) == 2:
                right[node] = children[1]

    calculator(1)
    print(f'#{tc}', int(tree[1]))