import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    num_lst = list(map(int, input().split()))
    sum_result = 0
    for num in num_lst:  # 입력 받은 숫자 10개 탐색
        if num % 2 == 1:  # 홀수이면
            sum_result += num  # sum_result에 더하기
    print(f'#{tc} {sum_result}')  # 결과 출력