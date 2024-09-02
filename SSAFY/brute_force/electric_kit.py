# 완전검색_전자카트
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def perm(idx, v, total_v):                  # idx: 방문한 구역 개수(사무실 제외), v: 현재 구역, total_v: 총 배터리 소비량
    global min_v, visited

    if total_v >= min_v:                    # 현재 경로 가는 중에 총 배터리 소비량이 최소값을 이미 넘었으면
        return                              # 이 경로는 최소값이 될 가능성이 없음 (가지치기)

    for i in range(1, N):                   # 사무실 제외 1 ~ N-1번 구역까지 방문
        if not visited[i]:                  # 방문한적 없으면 방문
            visited[i] = 1                  # 해당 구역 방문 표시
            perm(idx + 1, i, total_v + arr[v][i])
            visited[i] = 0                  # 다른 경로 가야하니 방문 표시 지우기

    if idx == N - 1:
        total_v += arr[v][0]                # 사무실로 돌아오기
        min_v = min(min_v, total_v)         # 총 소비량이 최소 소비량보다 작으면 최소 소비량 갱신
        return


for tc in range(1, int(input())+1):
    N = int(input())                                                # 관리 구역 개수
    arr = [list(map(int, input().split())) for _ in range(N)]       # 배터리 소비량 배열
    visited = [0] * N                                               # 방문 리스트
    min_v = 100 * N                                                 # 최소 배터리 소비량 (초기값 설정)

    visited[0] = 1                                                  # 0번(사무실) 방문 표시
    perm(0, 0, 0)
    print(f'#{tc}', min_v)