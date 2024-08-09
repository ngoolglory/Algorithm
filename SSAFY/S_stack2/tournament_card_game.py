import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def find_winner(s, e):
    if s == e:                      # 그룹이 계속 쪼개지다가 결국 한명만 남으면
        return s         # 그 한명을 리턴
    else:                               # 재귀 타고 올라가자
        mid = (s + e) // 2              # 가운데 인덱스 계산
        lwin = find_winner(s, mid)      # 왼쪽 그룹
        rwin = find_winner(mid+1, e)    # 오른쪽 그룹

        # 재귀 타고 왔으니 계산해보자 누가 이겼냐
        if card_list[lwin] == 1 and card_list[rwin] == 3:     # 왼쪽이 가위, 오른쪽이 보
            return lwin                                       # 왼쪽 승
        elif card_list[lwin] == 3 and card_list[rwin] == 1:   # 왼쪽이 보, 오른쪽이 가위
            return rwin                                       # 오른쪽 승
        elif card_list[lwin] > card_list[rwin]:
            return lwin                                       # 왼쪽 승
        elif card_list[lwin] < card_list[rwin]:
            return rwin                                       # 오른쪽 승
        else:                                                 # 비겼으면
            # 번호가 작은 쪽을 승자로 함
            if lwin > rwin:
                return rwin
            else:
                return lwin

for tc in range(1, 1+int(input())):
    N = int(input())    # 인원 수
    card_list = list(map(int, input().split()))     # 카드 리스트
    answer = find_winner(0, N - 1)
    print(f'#{tc}', answer+1)