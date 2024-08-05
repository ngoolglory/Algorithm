# [S/W 문제해결 기본] 3일차 - 회문2

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def len_of_longest_palindrome(board):
    max_len = 0

    # 가로
    for r in range(100):
        for c in range(100):
            for end in range(100, c, -1):       # 회문인지 탐색할 문자열 대상의 끝 지점
                string = board[r][c:end]        # 현지점부터 끝지점까지의 문자열을 가져오기
                if string == string[::-1]:      # 가져온 문자열이 회문이면
                    if len(string) > max_len:   # 길이가 기존 최대 길이보다 크면
                        max_len = len(string)   # 최대 길이 갱신
                    break

    # 전치행렬 구하기
    for r in range(100):
        for c in range(100):
            if r < c:
                board[r][c], board[c][r] = board[c][r], board[r][c]

    # 세로
    for r in range(100):
        for c in range(100):
            for end in range(100, c, -1):  # 회문인지 탐색할 문자열 대상의 끝 지점
                string = board[r][c:end]  # 현지점부터 끝지점까지의 문자열을 가져오기
                if string == string[::-1]:  # 가져온 문자열이 회문이면
                    if len(string) > max_len:  # 길이가 기존 최대 길이보다 크면
                        max_len = len(string)  # 최대 길이 갱신
                    break

    return max_len


if __name__ == "__main__":
    for _ in range(10):
        tc = int(input())
        board = [list(input()) for _ in range(100)]
        answer = len_of_longest_palindrome(board)
        print(f'#{tc}', answer)
