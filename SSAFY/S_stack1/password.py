import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def password(N, string):
    stack = []
    for x in string:  # 문자열 내 숫자 순회
        if not stack:               # 스택이 비어 있으면
            stack.append(x)         # push
        else:                       # 스택이 비어 있지 않으면
            if stack[-1] == x:      # 스택의 top과 이번 원소가 같으면
                stack.pop()         # pop
            else:                   # 스택의 top과 이번 원소가 다르면
                stack.append(x)     # push
    return ''.join(stack)           # 스택에 남아 있는 숫자들을 붙여서 반환



if __name__ == "__main__":
    for tc in range(1, 11):
        N, string = input().split()   # N: 문자열의 총 수, string: 문자열
        answer = password(int(N), string)
        print(f'#{tc}', answer)