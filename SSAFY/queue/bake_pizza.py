import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def check_pizza_num(qsize, N, cheese_list):
    pizza_idx = 0   # 넣을 피자 인덱스
    Q = deque()     # 큐 생성
    Q.append([pizza_idx, cheese_list[pizza_idx]])
    pizza_idx += 1
    pizza_i = cheese_amount = 0     # 피자 번호, 치즈 양 (임시 변수)

    while len(Q) > 0:
        # 피자가 남아있는 선에서 큐가 꽉 찰 때까지 피자 집어 넣기
        while True:
            if len(Q) < qsize and pizza_idx < N:
                Q.append([pizza_idx, cheese_list[pizza_idx]])
                pizza_idx += 1
            else:
                break

        pizza_i, cheese_amount = Q.popleft()
        cheese_amount = cheese_amount // 2
        if cheese_amount > 0:
            Q.append([pizza_i, cheese_amount])

    return pizza_i + 1


for tc in range(1, 1+int(input())):
    qsize, N = map(int, input().split())    # qsize: 화덕의 크기, N: 피자의 개수
    cheese_list = list(map(int, input().split()))   # N개 피자에 뿌려진 치즈의 양
    answer = check_pizza_num(qsize, N, cheese_list)
    print(f'#{tc}', answer)