# [모의 SW 역량테스트] 요리사
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def synerge(recipe):
    score = 0
    for first in range(N//2):
        for second in range(first+1, N//2):
            score += arr[recipe[first]][recipe[second]] + arr[recipe[second]][recipe[first]]
    return score
    

def DFS(idx, k):
    global MIN_DIFF
    
    if idx == N//2:
        A = []
        B = []
        for j in range(N):
            if visited[j]:
                A.append(j)
            else:
                B.append(j)
        A_total = synerge(A)
        B_total = synerge(B)
        diff = abs(A_total - B_total)
        if diff < MIN_DIFF:
            MIN_DIFF = diff
        return
        
    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            DFS(idx+1, i+1)
            visited[i] = 0
    

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    MIN_DIFF = float('inf')
    
    DFS(0, 0)    
    print(f'#{tc} {MIN_DIFF}')