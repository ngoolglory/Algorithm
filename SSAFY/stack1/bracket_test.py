import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def check_bracket(code):
    size = len(code)
    stack = [0] * size
    top = -1
    i = 0
    pair_dict = {')':'(', '}':'{'}   # 괄호 짝을 묶어 놓은 딕셔너리

    while top >= -1 and i < size:
        if code[i] in pair_dict.values():      # 이번 원소가 여는 괄호이면
            top += 1            # push
            stack[top] = code[i]
        elif code[i] in pair_dict.keys():      # 이번 원소가 닫는 괄호이면
            if stack[top] != pair_dict[code[i]]:   # 짝이 맞지 않으면
                return 0
            else:                                 # 짝이 맞으면
                top -= 1        # pop
                v = stack[top+1]
        i += 1

    if top != -1:   # 스택이 비어있지 않거나, 언더플로우 발생 시
        return 0
    else:           # 스택이 비어 있고, 언더플로우가 발생하지 않았다면
        return 1

if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        code = input()
        answer = check_bracket(code)
        print(f'#{tc}', answer)