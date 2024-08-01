num = int(input())  # 숫자 입력 받기

for i in range(1, num+1):  # 1부터 num+1까지 loop
    if num % i == 0:  # 입력 받은 숫자를 i로 나누었을 때의 나머지가 0이면
        print(i, end=' ')  # i를 출력