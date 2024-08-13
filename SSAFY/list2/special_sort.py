# 배열2_특별한정렬_확인용

def special_sort(arr_size, arr):
    find_max = True  # 최대값 구하기 여부

    for i in range(arr_size-1):
        min_max_idx = i              # 최소값, 최대값 초기화

        for j in range(i+1, arr_size):
            if find_max:  # 최대값 찾을 순서이면
                if arr[j] > arr[min_max_idx]:  # 현재값이 최대값보다 크면
                    min_max_idx = j            # 최대값 갱신
            else:         # 최소값 찾을 순서이면
                if arr[j] < arr[min_max_idx]:  # 현재값이 최소값보다 작으면
                    min_max_idx = j            # 최소값 갱신
        arr[i], arr[min_max_idx] = arr[min_max_idx], arr[i]   # 맨 앞 값과 자리 바꾸기

        # 최대값 찾았으면 다음은 최소값, 최소값 찾았으면 다음은 최대값
        find_max = not find_max

    # 최종 결과를 출력하되, 숫자 10개까지 출력
    for i in range(10):
        print(arr[i], end=' ')


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        arr_size = int(input())                 # 정수의 개수
        arr = list(map(int, input().split()))   # 정수 리스트
        print(f'#{tc}', end=' ')     # 테스트 케이스 번호 출력
        special_sort(arr_size, arr)  # 정렬 결과 출력
        print()