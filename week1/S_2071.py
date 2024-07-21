import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    num_lst = list(map(int, input().split()))
    mean_result = round(sum(num_lst) / len(num_lst))  # 받은 숫자의 총합을 갯수로 나눈 뒤 반올림
    print(f'#{tc} {mean_result}')  # 결과 출력