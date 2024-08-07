import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def find_path(s, e):
    global adj_list, visited
    stack = []

    stack.append(s)             # 시작 노드를 stack에 넣고 시작
    visited[s] = True           # 스택에 들어갔으니 방문한 것

    # 시작노드부터 인접리스트를 타고가며 연결되어 있는 노드들 모두 순회
    while stack:
        popped_x = stack.pop()    # 스택의 top 원소를 pop (인접리스트 확인)
        if popped_x == e:         # 스택에서 도착 노드가 pop 된다는 것은 출발 노드 연결되어 있었다는 것을 의미하므로
            return 1              # 1 반환

        for i in adj_list[popped_x]:     # 해당 노드의 인접 노드들을 순회
            if not visited[i]:           # 방문한 적이 없으면
                visited[i] = True        # 방문했다고 기록
                stack.append(i)          # 방문한 적이 없는 인접 노드 스택에 넣기

    return 0    # 이 라인까지 왔다는 건 스택에 도착 노드가 들어오지 않았다는 것이므로 0 반환


if __name__ == "__main__":
    for _ in range(10):
        tc, N = map(int, input().split())               # 테스트케이스 번호, 길의 개수
        edge_list = list(map(int, input().split()))     # 길 리스트
        visited = [False] * (100)                       # 방문 리스트 초기화 (가능한 노드 번호 0~99)
        adj_list = [[] for _ in range(100)]             # 인접 리스트 초기화
        # 인접 리스트 채우기
        for i in range(0, len(edge_list), 2):
            adj_list[edge_list[i]].append(edge_list[i+1])
        s, e = 0, 99                                    # 출발노드, 도착노드
        answer = find_path(s, e)
        print(f'#{tc}', answer)