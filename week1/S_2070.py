import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    n1, n2 = map(int, input().split())
    print(f'#{tc}', end=' ')  # test case 번호 먼저 출력
    
    # 조건에 맞게 결과 출력
    if n1 > n2:
        print('>')
    elif n1 < n2:
        print('<')
    else:
        print('=')