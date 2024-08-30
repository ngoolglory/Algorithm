# 이진수 표현 
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

# 인덱스로 풀기
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 이진수 표현의 마지막 N개 비트, M: 이진수 표현할 십진수
    M = str(bin(M))                     # 십진수 M의 이진수 표현

    print(f'#{tc}', end=' ')
    for i in range(1, N+1):
        if M[-i] != '1':                # 뒤에서부터 읽을 때 '1'이 아닌 문자를 하나라도 만나면
            print('OFF')                # OFF
            break
    else:                               # 다 1이면
        print('ON')                     # ON


# 비트 연산자로 풀기
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 이진수 표현의 마지막 N개 비트, M: 이진수 표현할 십진수

    print(f'#{tc}', end=' ')
    for idx in range(N):
        if M & (1 << idx):              # 비트 1을 왼쪽으로 밀면서 M과 AND 연산 비교
            continue
        else:
            print('OFF')
            break
    else:
        print('ON')