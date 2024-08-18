# 스위치 켜고 끄기
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline
'''
- 남자: 받은 수의 배수인 스위치 상태 바꾸기
- 여자: 받은 수와 같은 번호인 스위치를 중심으로 좌우 대칭이면서,
가장 많은 스위치를 포함하는 구간의 스위치 상태 모두 바꾸기
'''
N = int(input())                                  # N: 스위치의 개수
switch_lst = list(map(int, input().split()))      # 스위치 상태 목록
student_N = int(input())                          # student_N: 학생 수

for _ in range(student_N):
    gender, num = map(int, input().split())       # 성별, 숫자 받기
    # 남자인 경우
    if gender == 1:
        for i in range(N):
            if (i+1) % num == 0:                   # 받은 수의 배수번째 스위치인 경우
                switch_lst[i] = 1 - switch_lst[i]  # 상태 바꾸기
    # 여자인 경우
    else:
        # 기준 중앙 스위치 지정 후 상태 바꾸기
        center = num - 1                           
        switch_lst[center] = 1 - switch_lst[center]
        # 기준으로부터 양쪽으로 퍼져나가면서 스위치 체크
        for k in range(1, N//2+1):
            left = center - k                      # 왼쪽 스위치
            right = center + k                     # 오른쪽 스위치
            # 유효한 위치이면서 두 스위치의 상태가 같으면 상태 바꾸기
            if 0 <= left < N and 0 <= right < N and switch_lst[left] == switch_lst[right]:
                switch_lst[left] = 1 - switch_lst[left]
                switch_lst[right] = 1 - switch_lst[right]
            else:
                break

# 최종 스위치 상태 한 줄에 20개씩 출력
for i in range(N):
    if i != 0 and i % 20 == 0:
        print()
    print(switch_lst[i], end=' ')