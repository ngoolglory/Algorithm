import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

P, K = map(int, input().split())
check = abs(P-K) + 1  # P에서 K를 뺀 값에 절대값을 씌우고, 1을 더하기
print(check)  # 결과 출력


    
