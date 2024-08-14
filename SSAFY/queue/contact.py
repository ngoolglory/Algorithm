# [S/W 문제해결 기본] 10일차 - Contact
import sys
sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')

from collections import deque

def BFS(start):
    global visited
    queue = deque()         # 큐 생성
    queue.append(start)     # 시작점 enqueue
    visited[start] = 1      # 시작점 방문 표시 (자기 자신 거리 1로 시작)

    while queue:        # 큐가 텅 빌 때까지 반복
        v = queue.popleft()         # dequeue
        for i in adj_dict[v]:       # dequeue 한 노드의 인접 리스트 순회
            if not visited[i]:      # 방문 아직 안한 노드면
                queue.append(i)     # enqueue
                visited[i] = visited[v] + 1     # 해당 노드로부터 1만큼 이동 (거리가 누작돼서 결국 시작점으로부터의 거리가 나옴)

    # 시작점으로부터 최대 거리
    max_dist = max(visited)

    # 방문 리스트 순회하며 최대 거리인 노드들 찾기
    highest_num = 0
    for idx in range(len(visited)):
        if visited[idx] == max_dist:      # 최대 거리 노드면
            if idx > highest_num:         # 가장 번호가 큰 사람
                highest_num = idx

    # 최대 거리 노드들 중 번호가 가장 큰 사람
    return highest_num


for tc in range(1, 11):
    data_len, start = map(int, input().split())     # data_len: 입력 받는 데이터 길이, start: 시작점
    data = list(map(int, input().split()))          # data: 숫자들 {from, to}쌍들

    # 인접 딕셔너리 만들기
    adj_dict = {}
    before_key = 0
    for i in range(data_len):
        if i % 2 == 0:                          # 짝수 인덱스면
            before_key = data[i]                # 이번 키 저장해놓고
            if data[i] not in adj_dict.keys():  # 인접 딕셔너리 키에 아직 없으면
                adj_dict[data[i]] = set()       # 인접 딕셔너리 키에 추가 (value 중복 제거를 위해 set로 만듦)
        else:                                   # 홀수 인덱스면
            if data[i] not in adj_dict.keys():  # 인접 딕셔너리 키에 아직 없으면
                adj_dict[data[i]] = set()       # 도착 노드지만 키를 만들어주긴 해야해
            adj_dict[before_key].add(data[i])   # 바로 전에 나왔던 키의 인접 리스트에 추가

    # 방문 리스트 만들기
    visited = [0] * (max(adj_dict) + 1)

    answer = BFS(start)
    print(f'#{tc}', answer)