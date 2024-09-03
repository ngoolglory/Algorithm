# 탐욕_베이비진 게임
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def check_run_triplet(visited, i):
    # run 확인
    if visited[i] == 3:
        return True
    # triplet 확인
    l2, l1, r1, r2 = i-2, i-1, i+1, i+2
    if 0 <= l2 and visited[l2] and visited[l1]:
        return True
    elif 0 <= l1 and r1 < 10 and visited[l1] and visited[r1]:
        return True
    elif r2 < 10 and visited[r1] and visited[r2]:
        return True 


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))       # 숫자 배열
    
    visited1 = [0] * 10                         # 0~9 인덱스를 가진 player1의 방문 배열
    visited2 = [0] * 10                         # 0~9 인덱스를 가진 player2의 방문 배열
    print(f'#{tc}', end=' ')
    for i in range(0, 12):
        if i % 2 == 0:
            visited1[arr[i]] += 1
            if check_run_triplet(visited1, arr[i]):
                print(1)
                break
        else:
            visited2[arr[i]] += 1
            if check_run_triplet(visited2, arr[i]):
                print(2)
                break
    else:
        print(0)