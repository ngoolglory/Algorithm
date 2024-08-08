import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def Calculator(formula):
    stack = [0] * len(formula)
    top = -1

    for token in formula:
        if token == '.':        # 토큰이 '.'이면
            break               # 반복문 종료
        elif token.isdigit():   # 토큰이 숫자면
            top += 1            # push
            stack[top] = token
        else:                   # 토큰이 연산자면
            if top < 1:         # 스택에 있는 숫자 개수가 2개 미만이면
                return 'error'  # 에러 출력
            # 스택에 숫자가 2개 이상 있으면
            top -= 2
            n1 = int(stack[top+1])
            n2 = int(stack[top+2])
            # 연산자 토큰의 종류에 따라 계산
            if token == '-':
                cal_result = n1 - n2
            elif token == '+':
                cal_result = n1 + n2
            elif token == '*':
                cal_result = n1 * n2
            else:
                cal_result = n1 // n2
            # 스택에 연산 결과 push
            top += 1
            stack[top] = cal_result

    # 끝났는데 스택에 숫자가 2개 이상 남아 있으면 에러
    if top > 0:
        return 'error'

    # 마지막에 스택에 남은 숫자가 최종 연산 결과
    return stack[0]


for tc in range(1, int(input())+1):
    formula = input().split()           # 문자열 계산식
    answer = Calculator(formula)        # 계산기 가동
    print(f'#{tc}', answer)