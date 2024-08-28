# 트리_이진힙_확인용
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from heapq import heappush

for tc in range(1, int(input())+1):
    N = int(input())                            # 자연수 개수
    num_lst = list(map(int, input().split()))   # 숫자 리스트
    parent_sum = 0                              # 조상 합
    heap = []                                   # 최소힙을 구현하기 위한 리스트
    for num in num_lst:                         # 숫자 리스트의 모든 숫자 순회
        heappush(heap, num)                     # 모두 최소힙에 넣기

    last_node = N                               # 마지막 노드
    while last_node > 1:                        # 루트에 도달할 때까지 반복
        last_node //= 2                         # 현재 노드의 부모 노드 찾기
        parent_sum += heap[last_node - 1]       # 조상 노드 값의 합 변수에 현재 부모 노드 값 더하기 (누적합)

    print(f'#{tc}', parent_sum)