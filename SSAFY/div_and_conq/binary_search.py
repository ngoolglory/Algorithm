# 분할정복_이진탐색
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
#sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())        # N: A 리스트 크기, M: B 리스트 크기
    A = sorted(list(map(int, input().split())))  # 리스트 A를 정렬
    B = list(map(int, input().split()))     # 리스트 B
    
    cnt = 0
    for b in B:                             # 리스트 B 원소 순회
        cur_area = -1                       # 현재 탐색 구간 (0: left, 1: right)
        l, r = 0, N-1                       # 왼쪽, 오른쪽 포인터
        
        while l <= r:                       # l이 r보다 커지면 반복 종료
            mid = (l + r) // 2              # 중간 인덱스 구하기
            
            if b < A[mid]:                  # b가 A의 mid 인덱스 값보다 작으면
                if cur_area != 0:           # 이전 탐색 방향이 왼쪽이 아니면
                    cur_area = 0
                else:                       # 같은 방향으로 반복 이동 시 중단
                    break
                r = mid - 1                 # 오른쪽 포인터를 mid-1로 이동
            elif b > A[mid]:                # b가 A의 mid 인덱스 값보다 크면
                if cur_area != 1:           # 이전 탐색 방향이 오른쪽이 아니면
                    cur_area = 1
                else:                       # 같은 방향으로 반복 이동 시 중단
                    break
                l = mid + 1                 # 왼쪽 포인터를 mid+1로 이동
            else:                           # b와 A[mid]가 같은 경우
                cnt += 1                    # 일치하는 경우 카운트 증가
                break
    
    print(f'#{tc} {cnt}')