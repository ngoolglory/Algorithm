# [S/W 문제해결 기본] 5일차 - GNS

import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

zero_to_nine = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
translator = dict(zip(zero_to_nine, range(10)))   # {'ZRO':0, 'ONE':1, ..., 'NIN':9}
back_translator = dict(zip(range(10), zero_to_nine))   # {0:'ZRO', 1:'ONE', ..., 9:'NIN'}

def sort_numbers(N, data):
    global translator, back_translator

    temp = ['' for _ in range(N)]  # 정렬된 배열
    counts = []  # 카운트 배열

    k = 9   # 0~9
    counts = [0] * (k+1)   # 0부터 k까지이므로 k+1 칸 할당

    # 카운팅 정렬 사용
    # 1단계 : data 원소 별 개수 세기
    for x in data:                  # data의 원소 x를 가져와서 번역한 뒤 카운트 배열에 개수 기록
        counts[translator[x]] += 1

    # 2단계 : 카운트 배열 누적합 구하기
    for i in range(1, k+1):         # count[1] ~ count[k]까지 누적 개수
        counts[i] += counts[i-1]

    # 3단계 : data의 맨 뒤부터 temp에 자리 잡기
    for i in range(N-1, -1, -1):
        translated_data = translator[data[i]]
        counts[translated_data] -= 1    # 누적 개수 1개 감소
        temp[counts[translated_data]] = back_translator[translated_data]

    return temp

if __name__ == "__main__":
    T = int(input())   # 테스트케이스 개수
    for tc in range(1, T+1):
        _, N = input().split()    # N: 단어의 갯수
        words = input().split()
        answer = sort_numbers(int(N), words)
        print(f'#{tc}', *answer)
