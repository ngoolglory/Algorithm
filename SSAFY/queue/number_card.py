import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

for tc in range(1, 1+int(input())):
    Q = deque([i for i in range(1, 1+int(input()))])
    cnt = 0
    # 카드 하나 남을 때까지 주어진 행동 반복
    while len(Q) > 1:
        cnt += 1
        card = Q.popleft()          # 일단 가장 위에 있는 카드 하나 뽑아
        if cnt % 2 == 0:            # 카운트가 짝수면
            Q.append(card)          # 카드 아래로 옮겨
    print(f'#{tc}', Q.popleft())    # 가장 마지막 남는 카드 출력