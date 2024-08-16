# 자기 방으로 돌아가기
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())  # N: 돌아가야 할 학생들의 수
    corridor = [0] * 201  # 각 복도 구간마다 학생이 몇 명 지나가는지 카운트

    for _ in range(N):
        s, e = map(int, input().split())  # s: 현재 방, e: 돌아갈 방
        # s가 더 크면 e와 swap (시작 방을 더 작게 설정 => 바꿔도 어차피 경로는 똑같음)
        if s > e:
            s, e = e, s

        # 방을 1~200 구간에 맞게 변환
        s = (s + 1) // 2
        e = (e + 1) // 2

        # 경로가 겹치는 구간에 대해 모두 카운트
        for i in range(s, e + 1):       # s ~ e
            corridor[i] += 1

    # 가장 많은 학생이 지나가는 구간의 최대값을 구함 (가장 많이 겹치는 곳을 해결하는 시간이 곧 최종적으로 걸리는 시간)
    time = max(corridor)

    print(f'#{tc}', time)