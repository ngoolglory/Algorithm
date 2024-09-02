# [S/W 문제해결 응용] 2일차 - 최대 상금
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def backtrack(cnt, pos, arr):
    global max_prize

    current_state = (cnt, ''.join(arr))                     # (현재 카운트, 배열 상태) 쌍을 저장
    if current_state in memo:                               # memo에 이미 똑같은 (현재 카운트, 배열 상태) 쌍이 있으면
        return                                              # 가지치기
    memo.add(current_state)                                 # 아직 나오지 않은 케이스면 memo에 저장
    
    if cnt == N:                                            # 주어진 교환 횟수에 도달했으면
        max_prize = max(max_prize, int(''.join(arr)))       # 최대 상금과 비교해서 최대 상금 갱신 
        return

    for i in range(pos, len(arr)):                          # pos부터 len(arr)-1까지 순회
        for j in range(i + 1, len(arr)):                    # i + 1부터 len(arr)-1까지 순회
            arr[i], arr[j] = arr[j], arr[i]                 # 스왑하기
            backtrack(cnt + 1, i, arr)                      # 다음 교환 시도
            arr[i], arr[j] = arr[j], arr[i]                 # 다시 스왑해서 원상태로 복구


for tc in range(1, 1+int(input())):
    arr, N = input().split()                                # arr: 숫자판, N: 교환 횟수
    arr, N = list(arr), int(N)                              # arr는 리스트로 만들고, 교환 횟수를 int로 바꾸기
    memo = set()                                            # 메모이제이션을 위한 set
    max_prize = 0                                           # 최대 상금

    backtrack(0, 0, arr)
    print(f'#{tc}', max_prize)