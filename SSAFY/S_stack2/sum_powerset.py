import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def powerset_sum(k, N, s, key):    # k: 원소, N: 집합의 크기, s: i-1까지 고려된 합, key: 목표
    global cnt

    if s > key:  # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif sum(bit) == N:  # 원소 갯수가 N개이면서
        if s == key:     # N개 원소 합이 key인 경우
            cnt += 1
        return
    else:  # 고려한 원소의 합이 찾는 합보다 작은 상태이고, 아직 트리의 끝까지 오지 않은 상태
        bit[k] = 1
        powerset_sum(k + 1, N, s + arr[k], key)  # arr[i] 포함
        bit[k] = 0
        powerset_sum(k + 1, N, s, key)  # arr[i] 미포함


for tc in range(1, 1+int(input())):
    N, key = map(int, input().split())     # N: 부분집합 원소의 수, key: 부분 집합의 목표 합
    arr = [i for i in range(1, 13)]  # 배열 생성 1~12
    bit = [0] * 13
    cnt = 0  # 합이 key인 부분집합의 개수
    powerset_sum(0, N, 0, key)
    print(f'#{tc}', cnt)