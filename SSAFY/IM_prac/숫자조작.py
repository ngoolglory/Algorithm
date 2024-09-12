# 13428. 숫자 조작
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")


for tc in range(1, 1+int(input())):
    arr = list(input().strip())
    max_num = 0
    min_num = 1e9
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] == '0' and i == 0:
                continue
            arr[i], arr[j] = arr[j], arr[i]
            tmp = int(''.join(arr))
            max_num = max(max_num, tmp)
            min_num = min(min_num, tmp)
            arr[i], arr[j] = arr[j], arr[i]

    if min_num == 1e9:
        min_num = 0

    print(f'#{tc}', min_num, max_num)