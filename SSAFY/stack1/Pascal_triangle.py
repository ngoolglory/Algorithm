import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def Pascal(n):
    if n == 1:
        return [1]
    else:
        prev = Pascal(n-1)
        print(*prev)
        return [1] + [prev[i] + prev[i+1] for i in range(len(prev)-1)] + [1]


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        n = int(input())     # 파스칼 삼각형의 크기
        print(f'#{tc}')
        last_line = Pascal(n)
        print(*last_line)