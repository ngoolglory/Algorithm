# 퍼펙트 셔플
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    N = int(input())
    card_lst = input().split()
    mid = N // 2
    if N % 2 == 1:
        mid += 1
    deck1 = card_lst[:mid]
    deck2 = card_lst[mid:]
    
    new_card_lst = []
    for i in range(mid):
        if i == N//2:
            new_card_lst.append(deck1[i])
        else:
            new_card_lst.append(deck1[i])
            new_card_lst.append(deck2[i])
    
    print(f'#{tc}', *new_card_lst)