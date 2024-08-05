# [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def len_of_longest_palindrome(board):
    max_len = 0

    # 가로
    for r in range(100):
        for c in range(100):
            for end in range(100, c, -1):   # 회문인지 탐색할 문자열 대상의 끝 지점
                if (end - c) <= max_len:    # 현재 길이가 최대 길이보다 작거나 같으면 종료
                    break
                for i in range((end-c)//2):
                    if board[r][c + i] != board[r][end-i-1]:  # 회문 체크
                        break
                else:
                    curr_len = end - c
                    if max_len < curr_len:
                        max_len = curr_len

    # 전치행렬 구하기
    for r in range(100):
        for c in range(100):
            if r < c:
                board[r][c], board[c][r] = board[c][r], board[r][c]

    # 세로
    for r in range(100):
        for c in range(100):
            for end in range(100, c, -1):  # 회문인지 탐색할 문자열 대상의 끝 지점
                if (end - c) <= max_len:  # 현재 길이가 최대 길이보다 작거나 같으면 종료
                    break
                for i in range((end - c) // 2):
                    if board[r][c + i] != board[r][end - i - 1]:  # 회문 체크
                        break
                else:
                    curr_len = end - c
                    if max_len < curr_len:
                        max_len = curr_len

    return max_len


if __name__ == "__main__":
    for _ in range(10):
        tc = int(input())
        board = [list(input()) for _ in range(100)]
        answer = len_of_longest_palindrome(board)
        print(f'#{tc}', answer)
