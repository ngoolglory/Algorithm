# 진기의 최고급 붕어빵
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

# 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 여부를 판단하는 함수
def boongeobbang(N, M, K, arrive_time):
    arrive_time.sort()      # 손님 오는 시각 오름차순 정렬
    cur_sec = M             # 현재 시각 (초기값은 한번 구운 상태)
    cur_num = K             # 현재 남아 있는 붕어빵 개수 (초기값은 한번 구운 상태)
    for guest_sec in arrive_time:
        if cur_sec < guest_sec:                     # 아직 손님 오기 전이면
            while cur_sec + M <= guest_sec:         # 손님 올 때까지 계속 구워
                cur_sec += M
                cur_num += K
        if guest_sec - M < 0 or cur_num == 0:       # 너무 일찍 오거나 왔는데 붕어빵이 없으면
            return 'Impossible'                     # 못 줘
        cur_num -= 1                                # 손님 한명 왔으니 붕어빵 하나 줘
    return 'Possible'                               # 다 줬으면 성공

for tc in range(1, 1+int(input())):
    # N: 손님 수, M: 븡어빵 K개 만드는데 걸리는 시간, K: M초만에 만들 수 있는 붕어빵 수
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))       # 손님이 도착하는 시각
    answer = boongeobbang(N, M, K, arrive_time)
    print(f'#{tc}', answer)
