# 숫자를 정렬하자

def selection_sort(arr_size, arr):

    for i in range(arr_size-1):
        min_idx = i    # 최소값 초기화
        for j in range(i+1, arr_size):
            if arr[j] < arr[min_idx]:  # 현재값이 최소값보다 작으면
                min_idx = j            # 최소값 갱신
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # 맨 앞 값과 자리 바꾸기

    # 최종 결과 출력
    print(*arr)


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        arr_size = int(input())                 # 정수의 개수
        arr = list(map(int, input().split()))   # 정수 리스트
        print(f'#{tc}', end=' ')     # 테스트 케이스 번호 출력
        selection_sort(arr_size, arr)  # 정렬 결과 출력