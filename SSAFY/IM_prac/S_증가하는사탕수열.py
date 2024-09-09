# 증가하는 사탕 수열
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, -1, -1):
        if arr[i] < arr[i+1]:
            continue
        cur = arr[i]
        arr[i] = arr[i+1] - 1
        if arr[i] <= 0:
            print(f'#{tc}', -1)
            break
        ans += cur - arr[i]
    else:
        print(f'#{tc}', ans)