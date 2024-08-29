# 햄버거 다이어트
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def backtrack(idx, score_sum, cal_sum):
    global visited, max_score
    if cal_sum > L:                 # 경로 중간에 이미 제한 칼로리 넘어버리면 그 경로 가망 없음
        return                      # 가지치기
    
    if idx == N:                    # 최대 인덱스 도달 시
        if score_sum > max_score:   # 현재 점수 합이 기존 최대 점수보다 높으면
            max_score = score_sum   # 최대값 갱신
    else:                           # 아직 최대 인덱스 도달 못했으면
        visited[idx] = 1            # 해당 위치 방문했을 때의 경로 재귀 호출
        backtrack(idx + 1, score_sum + score_lst[idx], cal_sum + cal_lst[idx])
        visited[idx] = 0            # 해당 위치 방문 안했을 때의 경로 재귀 호출
        backtrack(idx + 1, score_sum, cal_sum)

for tc in range(1, int(input())+1):
    N, L = map(int, input().split())    # N: 재료의 수, L: 제한 칼로리
    visited = [0] * N                   # 방문 리스트
    max_score = 0                       # 최대 점수

    score_lst = []
    cal_lst = []
    for _ in range(N):
        score, cal = map(int, input().split())      # 점수, 칼로리 받기
        score_lst.append(score)
        cal_lst.append(cal)
    
    backtrack(0, 0, 0)
    
    print(f'#{tc}', max_score)