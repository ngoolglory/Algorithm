# [S/W 문제해결 기본] 3일차 - 회문1

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def num_of_palindromes(palin_len, board):
    cnt = 0

    # 가로
    for r in range(8):
        for c in range(8 - palin_len + 1):
            string = board[r][c:c+palin_len]   # 현지점부터 제시된 길이만큼의 문자열을 가져오기
            if string == string[::-1]:         # 해당 문자열이 회문이면
                cnt += 1                       # 카운트 1 증가

    # 전치행렬 구하기
    for r in range(8):
        for c in range(8):
            if r < c:
                board[r][c], board[c][r] = board[c][r], board[r][c]

    # 세로
    for r in range(8):
        for c in range(8 - palin_len + 1):
            string = board[r][c:c + palin_len]  # 현지점부터 제시된 길이만큼의 문자열을 가져오기
            if string == string[::-1]:  # 해당 문자열이 회문이면
                cnt += 1  # 카운트 1 증가

    return cnt


if __name__ == "__main__":
    for tc in range(1, 11):
        palin_len = int(input())
        board = [list(input()) for _ in range(8)]
        answer = num_of_palindromes(palin_len, board)
        print(f'#{tc}', answer)
