# 스택1_종이_붙이기 (메모이제이션 X)
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

# a(n) = a(n-1) + 2*a(n-2)
def attach_paper(n):
    if n == 1:      # n=1 이면
        return 1    # 1 반환
    elif n == 2:    # n=2 이면
        return 3    # 3 반환
    else:           # 3 이상이면
        return attach_paper(n-1) + 2*attach_paper(n-2)    # f(n-1) + 2*f(n-2) 재귀

if __name__ == '__main__':
    for tc in range(1, int(input())+1):
        n = int(input()) // 10      # 가로 길이 / 10
        answer = attach_paper(n)    # 가능한 경우의 수 찾기
        print(f'#{tc}', answer)