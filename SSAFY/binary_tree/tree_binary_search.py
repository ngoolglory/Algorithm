# 트리_이진탐색_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def in_order(node):         # 중위 순회
    global cnt              # cnt 하나씩 올려가면서 숫자를 채워넣을거니까 글로벌 변수 선언
    if node > N:            # 현재 노드 번호가 노드 최대 번호보다 크면 종료
        return
    in_order(node*2)        # 현재 노드 기준 왼쪽 노드 재귀
    tree[node] = cnt        # 왼쪽 끝 노드까지 갔으면 현재 카운트 집어넣고 
    cnt += 1                # 카운트 1 증가
    in_order(node*2+1)      # 현재 노드 기준 오른쪽 노드 재귀


for tc in range(1, int(input())+1):
    N = int(input())                # 트리의 노드 수
    tree = [None] * (N + 1)         # 트리 초기화
    cnt = 1                         # 카운트 초기화
    root = 1                        # 시작 뿌리 노드
    in_order(root)                  # 중위 순회하면서 노드를 방문할 때마다 1부터 숫자를 차례로 채우기
    print(f'#{tc}', tree[1], tree[N//2])