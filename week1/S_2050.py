import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

alphas = input()

# 아스키 코드 상, 대문자 A는 65에 해당함
# 대문자만 들어온다고 가정하면, 64를 빼면 됨
for alpha in alphas:
    ascii = ord(alpha)  # ord() 함수를 사용하여 문자를 아스키코드로 변환
    print(ascii - 64, end=' ')  # A를 1로 만들기 위해 64 빼기