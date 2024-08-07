import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def graph_path(n_node, n_edge):
    visited = [False] * (n_node + 1)  # 방문 리스트 초기화 (0 ~ 노드 개수 + 1)
    adj_list = [[] for _ in range(n_node + 1)]  # 인접 리스트 초기화
    stack = []

    # 인접 리스트 만들기
    for _ in range(n_edge):
        n1, n2 = map(int, input().split())  # 간선 연결된 노드 1, 노드 2
        adj_list[n1].append(n2)             # 방향성 고려 (일방향)
        #adj_list[n2].append(n1)            # 이 코드를 넣으면 양방향이 됨

    S_node, G_node = map(int, input().split())  # 경로의 존재를 확인할 출발노드, 도착노드

    stack.append(S_node)        # 시작 노드를 stack에 넣고 시작
    visited[S_node] = True      # 스택에 들어갔으니 방문한 것

    # 시작노드부터 인접리스트를 타고가며 연결되어 있는 노드들 모두 순회
    while stack:
        popped_x = stack.pop()    # 스택의 top 원소를 pop (인접리스트 확인)
        if popped_x == G_node:    # 스택에서 G_node가 pop 된다는 것은 S_node와 연결되어 있었다는 것을 의미하므로
            return 1              # 1 반환

        for i in adj_list[popped_x]:     # 해당 노드의 인접 노드들을 순회
            if not visited[i]:           # 방문한 적이 없으면
                visited[i] = True        # 방문했다고 기록
                stack.append(i)          # 방문한 적이 없는 인접 노드 스택에 넣기

    return 0    # 이 라인까지 왔다는 건 스택에 G_node가 들어오지 않았다는 것이므로 0 반환


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        n_node, n_edge = map(int, input().split())   # 노드 개수, 간선 개수
        answer = graph_path(n_node, n_edge)
        print(f'#{tc}', answer)