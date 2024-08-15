# 농작물 수확하기
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())                        # 농장 크기
    arr = [list(map(int, list(input()))) for _ in range(N)]     # 농장
    center = N//2                           # 중심 좌표
    crop_sum = 0                            # 농작물 합 초기값
    
    # 가장 윗 행부터 아래로 내려오면서 더하기
    # N이 7인 경우 센터는 7//2 = 3이므로 시작점은 3번 인덱스
    # 아래로 내려오면서 중간 행까지 1, 3, 5 칸씩 더하기 (칸수는 +2씩)
    # 아래쪽은 반대로
    # 위쪽 합(중간 행 포함) + 아래쪽 합
    
    start = center+1  # 위쪽은 center+1 열부터 시작 (1 빼고 시작할거니까)
    steps = -1        # 더할 칸 (2 더하고 시작할거니까)

    for r in range(N):
        
        # 위쪽 합 구하기
        if r <= center:
            start -= 1
            steps += 2
            for c in range(start, start+steps):
                crop_sum += arr[r][c]
        
        # 아래쪽 합 구하기
        else:
            start += 1
            steps -= 2
            for c in range(start, start+steps):
                crop_sum += arr[r][c]
                        
    print(f'#{tc}', crop_sum)