# 배열2_부분집합의합_확인용

def subset_whose_sum_is_K(N, K):
    arr = [i for i in range(1, 13)]
    n = len(arr)
    flag = False
    cnt = 0  # 원소의 합이 K인 부분집합의 개수

    # 부분집합 구하기
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])

        # 부분집합의 합 구하기
        if subset and len(subset) == N:  # 비어있지 않으면
            subset_sum = 0
            for num in subset:
                subset_sum += num

            # 부분집합의 원소의 합이 K이면 cnt 1 증가
            if subset_sum == K:
                flag = True
                cnt += 1

    # 만약 조건에 만족하는 subset이 없으면 0, 있으면 cnt 반환
    if flag:
        return cnt
    else:
        return 0


if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T + 1):
        N, K = map(int, input().split())  # N: 부분집합 원소 개수, K: 부분집합 원소의 합
        answer = subset_whose_sum_is_K(N, K)
        print(f'#{tc} {answer}')