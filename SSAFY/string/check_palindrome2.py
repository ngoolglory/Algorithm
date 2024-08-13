import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def check_palindrome(board_size, palin_size, board):
    # 행에서 찾기
    for r in range(board_size):
        for c in range(board_size - palin_size + 1):
            start = c
            end = c + palin_size - 1
            is_palin = True

            # 회문 검사
            while start <= end:
                if board[r][start] != board[r][end]:
                    is_palin = False
                    break
                start += 1
                end -= 1

            # 회문을 찾으면 해당 회문 반환
            if is_palin:
                string = ''
                for i in range(c, c + palin_size):
                    string += board[r][i]
                return string

    # 열에서 찾기
    for c in range(board_size):
        for r in range(board_size - palin_size + 1):
            start = r
            end = r + palin_size - 1
            is_palin = True

            # 회문 검사
            while start <= end:
                if board[start][c] != board[end][c]:
                    is_palin = False
                    break
                start += 1
                end -= 1

            # 회문을 찾으면 해당 회문 반환
            if is_palin:
                string = ''
                for i in range(r, r + palin_size):
                    string += board[i][c]
                return string


if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        board_size, palin_size = map(int, input().split())  # 글자판 크기, 회문 길이 입력
        board = [list(input()) for _ in range(board_size)]
        answer = check_palindrome(board_size, palin_size, board)
        print(f'#{tc}', answer)