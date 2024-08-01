import sys
sys.stdin = open("C:/Users/SSAFY/Downloads/sample_input.txt", "r")

num = int(input())

def factorial(num):  # 팩토리얼 재귀함수 만들기
    if num == 1: return 1  # num이 1이면 1리턴
    else: return num + factorial(num-1)  # num이 1이 아니면 num + factorial(num-1) 리턴

print(factorial(num))