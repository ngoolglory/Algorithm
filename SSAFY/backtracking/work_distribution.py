# 동철이의 일 분배
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def backtrack(depth, prob):
    global max_prob
    # 현재까지의 확률이 최대 확률보다 낮거나 같으면 가치치기 (계속 곱해지는 값이 0보다 작은 값이므로)
    if prob <= max_prob:
        return
    # 최대 깊이 도달하면 최대값 갱신
    if depth == N:
        max_prob = max(max_prob, prob)
        return
    # 최대 깊이 도달 전에는 재귀호출
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                backtrack(depth+1, prob*arr[depth][i]/100)
                visited[i] = 0


for tc in range(1, 1+int(input())):
    N = int(input())                                                # 직원 수
    arr = [list(map(int, input().split())) for _ in range(N)]       # 성공할 확률 테이블 
    visited = [0] * N                                               # 방문 리스트
    max_prob = 0                                                    # 최대 성공 확률
    backtrack(0, 1)
    print(f'#{tc} {max_prob * 100:.6f}')