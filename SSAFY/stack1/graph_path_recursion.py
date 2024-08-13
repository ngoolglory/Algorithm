import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def graph_path(v):
    global G

    # 만약 이번 노드가 도착 노드라면 1 반환
    if v == G:
        return 1

    visited[v] = True      # 이번 노드 방문 정보 표시

    for i in adj_list[v]:               # 인접 노드 순회
        if not visited[i]:              # 방문한 적 없으면
            if graph_path(i):           # 재귀 호출 결과가 1이면
                return 1                # 1 반환

    return 0    # 이 라인까지 왔다는 건 재귀 호출 결과 한번도 1을 반환하지 않았다는 것이므로 0 반환


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        V, E = map(int, input().split())            # 노드 개수, 간선 개수

        visited = [False] * (V + 1)                 # 방문 리스트 초기화 (0 ~ 노드 개수 + 1)
        adj_list = [[] for _ in range(V + 1)]       # 인접 리스트 초기화

        # 인접 리스트 만들기
        for _ in range(E):
            n1, n2 = map(int, input().split())  # 간선 연결된 노드 1, 노드 2
            adj_list[n1].append(n2)             # 방향성 고려 (일방향)
            # adj_list[n2].append(n1)           # 이 코드를 넣으면 양방향이 됨

        S, G = map(int, input().split())        # 경로의 존재를 확인할 출발노드, 도착노드

        print(f'#{tc}', graph_path(S))