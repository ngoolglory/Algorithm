# 배열2_이진탐색_확인용

def binary_search(total_pages, p):
    book = [i for i in range(1, total_pages+1)]
    start, end = 0, total_pages-1
    cnt = 0
    # 이진 탐색
    while start <= end:
        cnt += 1
        mid = int((start + end) / 2)
        if book[mid] == p:     # 목표 페이지 찾음
            return cnt
        elif book[mid] > p:
            end = mid
        else:
            start = mid

if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 수
    for tc in range(1, T + 1):
        p, pa, pb = map(int, input().split())  # p: 책의 전체 쪽 수, pa: A가 찾을 쪽 번호, pb: B가 찾을 쪽 번호
        a_cnt = binary_search(p, pa)  # A가 펼친 횟수
        b_cnt = binary_search(p, pb)  # B가 펼친 횟수

        # 누가 이겼는지 판단
        answer = ''
        if a_cnt > b_cnt:
            answer = 'B'
        elif a_cnt < b_cnt:
            answer = 'A'
        else:
            answer = 0
        print(f'#{tc}', answer)