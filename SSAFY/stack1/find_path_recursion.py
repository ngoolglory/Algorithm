import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

# 재귀로 풀기
def find_path(v):
    if v == 99:     # 만약 이번 노드가 도착 노드인 99이면
        return 1    # 1 반환

    visited[v] = True      # 이번 노드 방문

    # 전부 방문했으면 for문 내에 if문으로 들어가지 않기 때문에 재귀가 종료됨
    for i in adj_list[v]:
        if not visited[i]:          # 방문한 적 없으면
            if find_path(i):        # 거기로 가서 다시 인접 리스트 내 노드 조사 => 1 반환 되면
                return 1            # 1 반환

    return 0    # 끝까지 99에 도달하지 못했으면 0 반환


if __name__ == "__main__":
    for _ in range(10):
        tc, N = map(int, input().split())               # 테스트케이스 번호, 길의 개수
        edge_list = list(map(int, input().split()))     # 길 리스트

        visited = [False] * (100)                       # 방문 리스트 초기화 (가능한 노드 번호 0~99)
        adj_list = [[] for _ in range(100)]             # 인접 리스트 초기화

        # 인접 리스트 채우기
        for i in range(0, len(edge_list), 2):
            adj_list[edge_list[i]].append(edge_list[i+1])

        print(f'#{tc}', find_path(0))   # 0부터 출발해서 결과값 바로 출력