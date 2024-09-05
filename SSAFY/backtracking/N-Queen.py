# N-Queen
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def check(row):
    for r in range(row):                # 현재 행 이전 행만 보면 됨
        if visited[r] == visited[row]:  # 행들을 쭉 보면서 지금 컬럼에 퀸이 하나라도 놓여 있다면
            return False                # 그 컬럼엔 못놓아
        if abs(visited[r] - visited[row]) == abs(r - row):      # (열 인덱스 차이) == (행 인덱스 차이)
            return False
    return True

def backtrack(row):
    global cnt
    if row == N:                        # 끝 행에 도달했으면
        cnt += 1                        # 퀸 놓는 방법 수 1개 찾았어
        return                          # 찾았으니 이 경로는 탐색 종료
    else:
        for col in range(N):
            visited[row] = col          # 일단 거기 방문 표시 해봐 (어차피 col값이 갱신되니 방문표시 취소할 필요X)
            if check(row):              # 현재 col에 놓을 수 있는지 확인해보자
                backtrack(row+1)        # 놓을 수 있다면 놓고 다음 행으로 넘어가자


for tc in range(1, 1+int(input())):
    N = int(input())                            # 퀸 개수
    visited = [0] * N                           # 방문 리스트 (visited[row] = col)
    cnt = 0                                     # 퀸을 놓는 방법의 수
    backtrack(0)
    print(f'#{tc}', cnt)