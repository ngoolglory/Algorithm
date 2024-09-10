# 그래프_연산
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

from collections import deque

def cal(oper_idx, num):
    if oper_idx == 0:
        return num + 1
    if oper_idx == 1:
        return num - 1
    if oper_idx == 2:
        return num * 2
    if oper_idx == 3:
        return num - 10

def bfs(start, target):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == target:
            return cnt
        
        for oper_idx in range(4):
            result = cal(oper_idx, current)
            
            if 0 <= result <= 1000000 and result not in visited:
                visited.add(result)
                queue.append((result, cnt + 1))


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{tc}', ans)