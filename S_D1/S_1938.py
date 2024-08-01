import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")

a, b = map(int, input().split())  # 두 숫자 입력 받기

print(a+b)  # 덧셈
print(a-b)  # 뺄셈
print(a*b)  # 곱셈
print(a//b)  # 나눗셈 (소수점 이하의 숫자를 버리기 위해 몫을 출력)