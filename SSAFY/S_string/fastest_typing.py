# 가장 빠른 문자열 타이핑

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def num_of_typing(A, B):
    cnt = 0
    start = 0
    while len(A) - start >= len(B):
        for i in range(len(B)):
            if A[start+i] != B[i]:
                break
        else:
            start += len(B) - 1
            cnt += 1
        start += 1

    return len(A) - cnt*len(B) + cnt

if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        A, B = input().split()  # A: 타이핑할 전체 문자, B: 한번 눌러서 타이핑 가능한 문자열
        answer = num_of_typing(A, B)
        print(f'#{tc}', answer)