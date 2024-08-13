import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def find_min_sum(N, arr):
    min_sum = float('inf')  # 최소 합을 저장할 변수 마이너스 무한대로 초기화
    visited = [False] * N  # 각 열을 방문했는지 여부 저장

    def backtrack(row, current_sum):
        nonlocal min_sum    # 얘는 backtrack 함수 내부에서 바뀔거니까 nonlocal

        # 모든 행에서 숫자를 선택한 경우
        if row == N:
            if current_sum < min_sum:
                min_sum = current_sum
            return

        # 가지 치기 => 현재 합이 이미 최소 합을 초과한 경우 탐색 중단
        if current_sum >= min_sum:
            return

        # 현재 행에서 선택 가능한 열 탐색
        for col in range(N):
            if not visited[col]:  # 해당 열이 선택되지 않았다면
                visited[col] = True
                backtrack(row + 1, current_sum + arr[row][col])
                visited[col] = False  # 백트래킹을 위해 방문 표시 해제

    # 백트래킹 시작
    backtrack(0, 0)
    return min_sum

for tc in range(1, 1+int(input())):
    N = int(input())    # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열
    answer = find_min_sum(N, arr)
    print(f'#{tc}', answer)