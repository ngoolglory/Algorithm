# 계산기 1
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')


def Cal1(N, formula):
    isp = {'*':2, '/':2, '+':1, '-':1, '(':0}   # in-stack priority
    icp = {'*':2, '/':2, '+':1, '-':1, '(':3}   # in-coming priority
    stack = [0] * len(formula)
    top = -1
    result = ''

    for token in formula:
        if token.isdigit():     # 토큰이 숫자면
            result += token
        else:                   # 토큰이 연산자(괄호포함)이면
            if token == ')':    # 토큰이 오른쪽 괄호 ')'이면
                while stack[top] != '(':      # 왼쪽 괄호 '('가 나올 때까지 계속 pop
                    result += stack[top]      # pop 원소 출력
                    top -= 1
                top -= 1        # '('는 출력 없이 pop
            # 스택이 비어있거나 top이 현재 토큰보다 우선순위가 낮으면
            elif top == -1 or isp[stack[top]] < icp[token]:
                top += 1
                stack[top] = token      # push
            else:               # 스택에 원소가 들어있고, top이 현재 토큰보다 우선순위가 낮지 않으면
                # 현재 토큰보다 우선순위가 더 낮은 연산자가 나올 때까지 pop
                while top > -1:
                    if isp[stack[top]] < icp[token]:
                        break
                    if stack[top] != '(':       # 괄호가 아니면
                        result += stack[top]    # pop 원소 출력
                    top -= 1
                top += 1        # 현재 토큰 push
                stack[top] = token

    if stack:       # 스택이 비어있지 않으면
        while top > -1:    # 빈 스택이 될 때까지 pop
            if stack[top] not in ['(', ')']:    # 괄호가 아니면
                result += stack[top]            # pop 원소 출력
            top -= 1                            # pop

    return result


def Cal2(formula):
    stack = [0] * len(formula)
    top = -1

    for token in formula:
        if token.isdigit():  # 토큰이 숫자면
            top += 1         # push
            stack[top] = token
        else:                # 토큰이 연산자면
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

    # 마지막에 스택에 남은 숫자가 최종 연산 결과
    return stack[0]


for tc in range(1, 11):
    N = int(input())                    # 문자열 계산식의 길이
    formula = input()                   # 문자열 계산식
    answer = Cal2(Cal1(N, formula))     # 계산기 가동
    print(f'#{tc}', answer)