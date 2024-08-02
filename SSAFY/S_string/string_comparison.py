# 문자열_문자열비교_확인용

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def string_comparison(s1, s2):
    first_ch = s1[0]  # 비교 시작 조건을 위한 str1의 첫 문자
    for i in range(len(s2)-len(s1)+1):      # s2 인덱스 (0 ~ s2길이-s1길이+1)
        if s2[i] == first_ch:               # 해당 문자가 s1의 첫 글자와 같으면 비교 시작
            for j in range(1, len(s1)):     # 첫 글자는 이미 같은 것을 확인했으므로 그 다음 글자부터 비교
                if s2[i + j] != s1[j]:      # 하나라도 다른게 있으면
                    break                   # 다음 글자로 넘어가기
            else:  # 모든 글자가 같은 부분이면
                return 1  # 1 반환
    return 0                # 같은 부분이 하나도 없으면 0 반환

if __name__ == "__main__":
    T = int(input())   # 테스트케이스 개수
    for tc in range(1, T+1):
        str1 = input()
        str2 = input()
        answer = string_comparison(str1, str2)
        print(f'#{tc}', answer)
