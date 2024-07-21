import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    num_lst = list(map(int, input().split()))
    print(f'#{tc} {max(num_lst)}')  # 입력 받은 숫자들의 최댓값 출력