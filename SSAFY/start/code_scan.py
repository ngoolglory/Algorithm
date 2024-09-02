# [S/W 문제해결 응용] 1일차 - 암호코드 스캔
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

'''
<암호 규칙>
1. 숫자 8개로 구성
2. 앞 7자리는 상품 고유 번호, 마지막 자리는 검증 코드

<암호 검증법>
((홀수 자리의 합 * 3) + (짝수 자리의 합) + (검증 코드)) % 10 == 0

input().strip() 무조건 해야됨.. 인풋 원소가 서로 붙어있으면 ㅠㅠ
'''

# 암호 해독기 (0으로 구성되어 있는 앞부분 제외하고 2, 3, 4번째 부분 개수 비율)
decoder = {'211' : 0, '221' : 1, '122' : 2, '411' : 3, '132' : 4,
           '231' : 5, '114' : 6, '312' : 7, '213' : 8, '112' : 9}

# 16개의 숫자에 대한 2진수 표현
hex_dict = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

for tc in range(1, 1+int(input())):
    H, W = map(int, input().split())                        # H: 배열 세로, W: 배열 가로
    arr = list(set([input().strip() for _ in range(H)]))    # set으로 중복되는 행은 지우기
    arr = sorted(arr)[1:]                                   # 0만 있는 행은 제거
    answer = 0                                              # 올바른 검증코드의 각 숫자 합을 모두 더할 변수    
    code_history = []                                       # 지금까지 나왔던 암호 코드 넣을 리스트
    
    for row in arr:
        # 16진법으로 표현된 행을 2진법으로 바꾸기
        hex_row = ''
        for h in row:
            hex_row += hex_dict[h]
        # 왼쪽 0 다 지우기
        hex_row = hex_row.lstrip('0')

        cnt = 0                                 # 암호 자릿수 카운트
        part1 = part2 = part3 = 0               # part 1~3 사이즈 저장
        even = odd = 0                          # 홀수, 짝수 합 저장
        code = ''
        for ch in hex_row:                      # 이번 행에 있는 숫자들 쭉 순회
            # part 1,2,3 크기 채우기
            if ch == '1' and part2 == 0:
                part1 += 1
            elif ch == '0' and part1 > 0 and part3 == 0:
                part2 += 1
            elif ch == '1' and part2 > 0:
                part3 += 1
            # part 1,2,3 크기 다 채웠으면
            elif part3 > 0:
                cnt += 1                                    # 암호 한자리 들어옴
                # 무조건 part 1,2,3 비율 중에 1이 있기 때문에 최소값이 비율 1일 것임 (전체를 그걸로 나눠주면 됨)
                multiply = min(part1, part2, part3)         # 가로 크기 몇 배 늘어났는지
                # 늘어난 배수만큼 나눠주기
                ratio = map(lambda x: x//multiply, [part1, part2, part3])    
                key = ''.join(list(map(str, ratio)))        # 숫자였으니 문자로 바꾸고 합치기
                num = decoder[key]                          # 해독된 숫자
                code += str(num)                            # 해독된 숫자 하나씩 추가
                
                # 암호 길이가 8에 도달했고, 앞서 나왔던 암호가 아니면
                if len(code) == 8:
                    if (odd*3 + even + num) % 10 == 0 and code not in code_history:
                        answer += odd + even + num
                        code_history.append(code)
                    even = odd = cnt = 0                    # 홀수, 짝수 합 초기화
                    code = ''                               # 암호 코드 초기화
                # 암호 길이가 8에 도달하지 못했으면
                else:
                    if cnt % 2 == 1:                        # 홀수 합 모아주기
                        odd += num
                    else:                                   # 짝수 합 모아주기
                        even += num
                                
                part1 = part2 = part3 = 0                   # part 1~3 사이즈 초기화

    print(f'#{tc}', answer)