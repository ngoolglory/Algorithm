# start_이진수_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")
#input = sys.stdin.readline

for tc in range(1, 1+int(input())):
    # 16진수 문자열 => 2진수 문자열 변환
    # 방법1. 16개의 숫자에 대한 2진수 표현을 dict로 저장해서 사용
    hex_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    N, hexadecimal_num = input().split()
    ans = ''
    for h in hexadecimal_num:
        ans += hex_dict[h]

    print(f'#{tc}', ans)

    # 방법2. 16진수 한자리를 정수로 변환
    N, hexadecimal_num = input().split()
    ans = ''
    for ch in hexadecimal_num:
        num = int(ch, 16)
        # num의 하위 4개의 비트를 조사
        ans += '1' if num & 8 else '0'     # num & (1 << 3)
        ans += '1' if num & 4 else '0'    # num & (1 << 2)
        ans += '1' if num & 2 else '0'   # num & (1 << 1)
        ans += '1' if num & 1 else '0'   # num & (1 << 0)

    print(f'#{tc}', ans)