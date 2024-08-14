# 03_배열1_3 분할
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    N = int(input())    # 정수의 개수
    arr = list(map(int, input().split()))   # 정수 리스트
    min_diff = float('inf')

    # 나누는 기준 위치를 오른쪽 구간의 시작 위치로 설정
    for i in range(1, N-1):    # 첫번째 나누는 기준 위치
        for j in range(i+1, N):   # 두번째 나누는 기준 위치

            # 세 구간 내 합 나누기
            area1, area2, area3 = sum(arr[0:i]), sum(arr[i:j]), sum(arr[j:N])

            # 각 구간 내 합의 최대, 최소 구하기
            min_sum = min([area1, area2, area3])
            max_sum = max([area1, area2, area3])

            # 최대 최소 차이 구하고, 기존 최소값보다 작으면 갱신
            diff = max_sum - min_sum
            if diff < min_diff:
                min_diff = diff

    print(f'#{tc}', min_diff)