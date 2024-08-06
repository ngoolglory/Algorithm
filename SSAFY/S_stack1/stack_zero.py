import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def stack_zero(arr):
    stack = []
    stack_sum = 0

    for num in arr:  # 배열 내 정수 순회
        if num == 0:
            stack_sum -= stack.pop()
        else:
            stack.append(num)
            stack_sum += num

    return stack_sum


if __name__ == "__main__":
    for tc in range(1, int(input()) + 1):
        N = int(input())  # 정수의 개수
        arr = list(map(int, input().split()))  # 정수 배열
        answer = stack_zero(arr)
        print(f'#{tc}', answer)