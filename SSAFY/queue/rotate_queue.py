import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def rotate_arr(arr, n_rotate):
    arr = deque(arr)    # 큐 만들기

    # 주어진 회전 횟수만큼 회전
    for _ in range(n_rotate):
        arr.rotate(-1)

    return arr.popleft()    # 맨 앞의 숫자 반환

for tc in range(1, 1+int(input())):
    N, n_rotate = map(int, input().split())     # N: 숫자 개수, n_rotate: 회전 횟수
    arr = list(map(int, input().split()))       # 숫자 배열
    print(f'#{tc}', rotate_arr(arr, n_rotate))