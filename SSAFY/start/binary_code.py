# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

def code_check(code):
    odd_sum = 0                     # 홀수 자리 합
    even_sum = 0                    # 짝수 자리 합
    for i in range(8):
        if i % 2 == 0:              # 홀수 자리면
            odd_sum += code[i]      # 홀수 자리 합에 더하기
        else:                       # 짝수 자리면
            even_sum += code[i]     # 짝수 자리 합에 더하기

    result = odd_sum * 3 + even_sum

    if result % 10 == 0:            # 계산 결과 10의 배수면 올바른 암호코드
        return sum(code)            # 암호코드에 포함된 숫자의 합 출력
    return 0                        # 10의 배수 아니면 잘못된 암호코드이므로 0 반환


decoder = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
           '0110001' : 5,'0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

for tc in range(1, 1+int(input())):
    H, W = map(int, input().split())            # H: 배열 세로, W: 배열 가로
    arr = [list(input()) for _ in range(H)]     # 배열

    # 암호가 있는 한 행만 보면 되니까 그 행이 어딘지 찾기
    find_flag = False
    for r in range(H):
        for c in range(W-1, -1, -1):    # 암호의 마지막은 1이기 때문에 뒤에서부터 읽기
            if arr[r][c] == '1':        # 해당 행에서 가장 마지막에 있는 1이 암호의 끝
                find_flag = True
                break
        if find_flag:
            break
    
    code_row = arr[r][c+1-56:c+1]                   # 암호 비트 부분만 가져오기
    code = []                                       # 완성된 코드를 넣을 리스트 초기화
    for start in range(0, len(code_row), 7):        # 7칸씩 점프하며 시작지점 설정
        key = ''.join(code_row[start:start+7])      # 7개의 비트
        code.append(decoder[key])                   # 키를 해독 후 코드에 넣기

    print(f'#{tc}', code_check(code))