import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    a, b = map(int, input().split())  # a, b 입력 받기
    print(f'#{tc} {a//b} {a%b}')  # 몫, 나머지 출력