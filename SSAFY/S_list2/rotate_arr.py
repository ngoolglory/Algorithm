# 숫자 배열 회전
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

def rotate_arr(N, arr):
    new_arr = [[0]*N for _ in range(N)]
    result_arr = []

    # 90도 회전한 새로운 배열 생성
    for r in range(N):
        for c in range(N):
            new_arr[c][N-1-r] = arr[r][c]
    
    for r in range(N):
        string = ''
        for c in range(N):
            string += str(new_arr[r][c])
        result_arr.append(string)
    
    return result_arr


for tc in range(1, 1+int(input())):
    N = int(input())    # 배열 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 첫번째 회전
    arr1 = rotate_arr(N, arr)
    # 두번째 회전
    arr2 = rotate_arr(N, arr1)
    # 세번째 회전
    arr3 = rotate_arr(N, arr2)

    print(f'#{tc}')
    for i in range(N):
        for arr in [arr1, arr2, arr3]:
            print(arr[i], end=' ')
        print()
    
    