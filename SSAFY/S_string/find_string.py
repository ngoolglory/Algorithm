# [S/W 문제해결 기본] 3일차 - String

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r', encoding='utf-8')

def find_string(part_string, total_string):
    total_len = len(total_string)
    part_len = len(part_string)
    cnt = 0
    for i in range(total_len - part_len + 1):   # 비교 시작 위치
        for j in range(part_len):
            if total_string[i + j] != part_string[j]:
                break   # for j, 다음 글자부터 비교 시작
        else:
            cnt += 1   # 패턴 개수 1 증가
    return cnt


if __name__ == "__main__":
    for _ in range(10):
        tc = int(input())  # 테스트 케이스
        part_string = input()        # 찾을 문자
        total_string = input()  # 전체 문자
        answer = find_string(part_string, total_string)
        print(f'#{tc}', answer)