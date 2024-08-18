# 배수 스위치
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

bulbs = ['N'] + list(input().strip())   # 전구 상태 목록 (인덱스를 편리하게 확인하기 위해 앞에 N 붙이기)
N = len(bulbs)                          # 전구 개수
cnt = 0                                 # 스위치 누른 횟수
for i in range(1, N):
    if bulbs[i] == 'Y':                 # 켜져있는 전구를 만나면
        for j in range(i, N, i):        # 해당 번호 배수인 전구 상태 변경
            if bulbs[j] == 'Y':
                bulbs[j] = 'N' 
            else: 
                bulbs[j] = 'Y'
        cnt += 1                        # 스위치 한번 누름
print(cnt)