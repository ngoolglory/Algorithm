import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

num = input()

digit_sum = 0
for digit in num:  # 숫자의 각 자릿수 하나씩 탐색
    digit_sum += int(digit)  # 각 자릿수를 하나씩 digit_sum에 더하기
print(digit_sum)