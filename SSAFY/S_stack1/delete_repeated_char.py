import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def delete_repeated_char(string):
    stack = []

    for ch in string:                       # 두번째 문자열부터 문자열 내 글자 탐색
        if not stack or ch != stack[-1]:    # 스택이 비어 있거나, 이번 char가 스택의 top 원소와 다르면
            stack.append(ch)                # push
        else:                               # 스택에 원소가 있고, 이번 char가 스택의 top 원소와 같으면
            stack.pop()                     # pop

    return len(stack)


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        string = input()
        answer = delete_repeated_char(string)
        print(f'#{tc}', answer)