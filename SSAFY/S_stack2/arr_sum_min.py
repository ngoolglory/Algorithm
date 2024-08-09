import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

# def backtrack(r, c):
#     global num_check, col_check, min_sum
#     if r == N:
#         return
#
#     if len(num_check) == 3:
#         # 합 구하기
#         cur_sum = 0
#         for x in check:
#             cur_sum += x
#         # 합이 기존 최소합보다 작으면 최소합 갱신
#         if cur_sum < min_sum:
#             min_sum = cur_sum
#     else:
#         for c in range(3):
#             if c in col_check:
#                 continue
#             num_check.append(arr[r][c])
#             col_check.append(c)
#             backtrack(r+1, c)
#
# for tc in range(1, 1+int(input())):
#     N = int(input())    # 배열 크기
#     arr = [list(map(int, input().split())) for _ in range(N)]   # 배열
#     num_check = []
#     col_check = []
#     min_sum = 0
#     answer = backtrack(0, 0)
#     print(f'#{tc}', answer)


# arr = [1, 2, 1, 2]
# N, K = 4, 3
# bits = [0] * N
# def subset(k, n, cur_sum): # k: 함수호출의 깊이, 노드의 높이, for문의 중첩횟수
#     if k == n:             # cur_sum: 현재까지 선택한 요소의 합
#         print(bits, end=' ')
#         S = 0
#         for i in range(n):
#             if bits[i]:
#                 print(arr[i], end=' ')
#                 S += arr[i]
#         print('==>', S, cur_sum)
#     else:
#         bits[k] = 0     # k번 요소를 포함하지 않음
#         subset(k + 1, n, cur_sum)
#         bits[k] = 1     # k번 요소를 포함
#         subset(k + 1, n, cur_sum + arr[k])
#
# subset(0, N, 0)




def find_min_sum(N, arr):
    min_sum = float('inf')  # 최소 합을 저장할 변수, 초기에는 매우 큰 값으로 설정
    visited = [False] * N  # 각 열이 선택되었는지 여부를 저장하는 리스트

    def backtrack(row, current_sum):
        nonlocal min_sum

        # 모든 행에서 숫자를 선택한 경우
        if row == N:
            if current_sum < min_sum:
                min_sum = current_sum
            return

        # 가지 치기: 현재 합이 이미 최소 합을 초과한 경우 탐색 중단
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