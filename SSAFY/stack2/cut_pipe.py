# 쇠막대기 자르기
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    brackets = input()      # brackets : 쇠막대기, 레이저 배치
    n_cur_bar = 0           # 현재 레이저에 걸쳐 있는 쇠막대기의 수
    total_pieces = 0        # 전체 잘린 쇠막대기 조각의 수
 
    for i in range(len(brackets)):
        if brackets[i] == '(':              # 이번 문자가 ( 이면
            n_cur_bar += 1                  # 쇠막대기 시작
        else:                               # 이번 문자가 ) 이면
            if brackets[i-1] == '(':        # 바로 이전 문자가 ( 였으면 => 레이저
                n_cur_bar -= 1              # 앞에 ( 가 나왔을 때 쇠막대기인줄 알고 1을 더했지만 레이저였기 때문에 다시 1 빼기
                total_pieces += n_cur_bar   # 현재 레이저에 걸쳐 있는 쇠막대기의 수 만큼 전체 조각에 더하기
            else:                           # 바로 이전 문자가 ( 가 아니면 => 쇠막대기 끝단
                n_cur_bar -= 1              # 쇠막대기 하나 빼기
                total_pieces += 1           # 전체 조각에 하나 더하기
    

    print(f'#{tc}', total_pieces)