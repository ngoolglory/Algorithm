# 삼성시의 버스 노선
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())    # N: 버스 노선 개수
    s_e = []

    for _ in range(N):
        s, e = map(int, input().split())    # s 이상 e 이하인 정류장을 다니는 노선
        s_e.append((s, e))

    P = int(input())    # P: 버스 정류장 개수
    target_lst = []
    for _ in range(P):
        target_lst.append(int(input()))         # 몇번 지났는지 확인할 버스 정류장

    cnt_lst = [0] * P
    for s, e in s_e:
        for i in range(len(target_lst)):
            if s <= target_lst[i] <= e:
                cnt_lst[i] += 1

    print(f'#{tc}', *cnt_lst)