# 문자열_글자수

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def calcualte_num_of_words(s1, s2):
    max_cnt = 0  # s1에 있는 어떤 문자가 s2에 존재하는 갯수의 최대치
    cnt_dict = {}
    # s1에 있는 문자들을 cnt_dict의 key로 넣고, value는 0으로 설정
    for key in set(s1):
        cnt_dict.update({key:0})

    for ch in s2:                       # s2에 있는 문자 순회
        cnt = cnt_dict.get(ch, -1)      # s2에 있는 문자가 딕셔너리에 key로 존재하지 않으면 -1을 cnt에 할당
        if cnt != -1:                   # 이번 문자가 딕셔너리에 key로 존재하면
            cnt_dict[ch] += 1           # 해당 키의 값을 1 올리고
            if max_cnt < cnt_dict[ch]:  # 기존 갯수 최대치보다 크면
                max_cnt = cnt_dict[ch]  # 최대치 갱신

    return max_cnt


if __name__ == "__main__":
    T = int(input())   # 테스트케이스 개수
    for tc in range(1, T+1):
        str1 = input()
        str2 = input()
        answer = calcualte_num_of_words(str1, str2)
        print(f'#{tc}', answer)
