# 초심자의 회문 검사

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def check_palindrome(string):
    start = 0               # 시작 포인터
    end = len(string) - 1   # 끝 포인터
    while start <= end:     # 시작 포인터가 끝 포인터보다 오른쪽으로 가거나 같아지면 종료
        if string[start] != string[end]:  # 투 포인터 위치 문자가 서로 다르면
            return 0                      # 0 반환
        start += 1      # 시작 포인터 오른쪽으로 한 칸 이동
        end -= 1        # 끝 포인터 왼쪽으로 한 칸 이동
    return 1        # 투 포인터 위치 문자가 항상 서로 같았으면 1 반환

if __name__ == "__main__":
    T = int(input())   # 테스트케이스 개수
    for tc in range(1, T+1):
        string = input().strip()  # 입력 받은 문자열의 앞, 뒤 공백 제거
        answer = check_palindrome(string)
        print(f'#{tc}', answer)