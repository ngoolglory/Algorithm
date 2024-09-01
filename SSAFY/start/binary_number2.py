# start_이진수2_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

# 수학적인 개념 활용
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
        


# 백트래킹 활용
def backtrack(idx, value, bin_num):
    global answer
    if answer:
        return
    if idx == 14:
        return
    if value == num:
        answer = bin_num
    backtrack(idx+1, value + 2**(-idx), bin_num+'1')
    backtrack(idx+1, value, bin_num+'0') 

for tc in range(1, 1+int(input())):
    num = float(input())
    answer = ''
    backtrack(1, 0, '')
    if answer:
        print(f'#{tc}', answer)
    else:
        print(f'#{tc}', 'overflow')
        
        
        
# 교수님 모범 답안
T = int(input())
 
for test_case in range(1, T + 1):
    number = float(input())   # 0.125
 
    # 계속 2를 곱해서 1 이상일경우 1을 넣고, 숫자에서1을 빼줌, 1이면 1넣고 끝, 1보다 작으면 0을 넣음
    # 이진법이 들어갈 곳
 
    ans = []
    # 13이상이 필요하다면 overflow
    space = 0
    while space < 13 and number != 0:
 
        number = number * 2
 
        if number < 1:
            ans.append(0)            
        elif number >= 1:
            ans.append(1)
            number -= 1
         
        space += 1
 
    # print(ans)   # [1, 0, 1]
 
 
    # 빈 칸 없이 출력 & 13이상일 때 overflow 출력하기
    # 13자리 이상 넘어간다면
    if space >= 13:
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case}', end=' ')
        for i in ans:
            print(i, end='')
        print()