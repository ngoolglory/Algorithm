# [S/W 문제해결 기본] 7일차 - 암호생성기
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def password_generator(arr):
    Q = deque(arr)  # 큐 생성
    i = 0  # 뺄 숫자 (i : 1~5)
    while True:
        i += 1
        pop_v = Q.popleft()  # pop 된 숫자
        # 감소된 숫자가 0보다 작거나 0이면 그냥 0으로 저장
        if pop_v - i <= 0:
            Q.append(0)
            return Q
        # 감소된 숫자가 0보다 크면
        else:
            Q.append(pop_v - i)  # 첫번째 숫자 i만큼 감소시키고 맨 뒤로 보내기
        # 사이클 다 돌았으면 다시 첨부터
        if i == 5:
            i = 0

for _ in range(10):
    tc = int(input())   # 테스트케이스 번호
    arr = list(map(int, input().split()))   # 배열
    answer = password_generator(arr)
    print(f'#{tc}', *answer)  # 최종 암호 배열 출력