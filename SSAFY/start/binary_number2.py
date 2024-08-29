# start_이진수2_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
<소수점 이진수로 변환하는 법>
1. 소수에 2 곱하기
2. 결과가 1로 나누어 떨어질 때까지 or 똑같은 소수부가 나올 때까지 반복
3. 정수부가 순서대로 소수점 뒤 이진수 결과가 됨
'''

for tc in range(1, 1+int(input())):
    decimal_num = float(input())           # 입력 받은 소수
    binary_num = ''                        # 2 곱했을 때 정수부 저장
    decimal_lst = []                       # 소수부 리스트
 
    while True:
        decimal_num *= 2                   # 2 곱했을 때 결과
        int_part = int(decimal_num)        # 정수부
        binary_num += str(int_part)        # 정수부는 이진수에 저장
        decimal_num -= int_part            # 소수부 저장

        # 소수부가 0이거나 똑같은 소수부가 나오면 반복 종료
        if decimal_num == 0 or decimal_num in decimal_lst:
            break

        decimal_lst.append(decimal_num)    # 나온 소수부는 리스트에 저장
    
    if len(binary_num) >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', binary_num)