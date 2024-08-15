# 추억의 2048게임
import sys
#sys.stdin = open('C:/Users/SSAFY/Downloads/sample_input.txt', 'r')
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

def stacking():
    global r, c, top, top_fusion, stack    
    if arr[r][c] == 0:      # 0이면 스택에 안넣고 그냥 통과
        return
    if top == -1:           # 스택 비어 있으면 그냥 스택에 넣기
        top += 1
        stack[top] = arr[r][c]
    else:                   # 스택에 원소가 있으면
        if stack[top] == arr[r][c]:     # top이랑 현 숫자가 같으면
            if not top_fusion:          # 합쳐진 숫자가 아니면
                stack[top] *= 2         # top 숫자 * 2
                top_fusion = True
            else:                       # 합쳐진 숫자면
                top += 1                # 그냥 스택에 넣기
                stack[top] = arr[r][c]
                top_fusion = False      # top은 이제 더이상 합쳐진 숫자가 아님  
        else:                           # top이랑 현 숫자가 다르면
            top += 1                    # 그냥 스택에 넣기
            stack[top] = arr[r][c]  
            top_fusion = False      # top은 이제 더이상 합쳐진 숫자가 아님
    
    
for tc in range(1, 1+int(input())):
    N, S = input().split()      # N: 배열 크기, S: 방향
    N = int(N)                  # N을 숫자로 바꿔주기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열
    final_arr = [[0]*N for _ in range(N)]   # 결과 배열
    
    # up: 가장 위 원소부터 스택에 넣기     
    if S == 'up':
        for c in range(N):
            # 스택에 집어 넣으면서 같은 숫자 있으면 더해서 합쳐주기
            stack = [0] * N         # N칸 스택 생성
            top = -1
            top_fusion = False      # top원소가 합쳐진 원소인지 아닌지 여부
            for r in range(N):
                stacking()            
            # 완성된 스택을 final arr에 넣어주기
            for r in range(N):
                final_arr[r][c] = stack[r]
                    
    # down: 가장 아래 원소부터 스택에 넣기      
    elif S == 'down':
        for c in range(N):
            # 스택에 집어 넣으면서 같은 숫자 있으면 더해서 합쳐주기
            stack = [0] * N         # N칸 스택 생성
            top = -1
            top_fusion = False      # top원소가 합쳐진 원소인지 아닌지 여부
            for r in range(N-1, -1, -1):
                stacking()
            # 완성된 스택을 final arr에 넣어주기
            for r in range(N):
                final_arr[N-1-r][c] = stack[r]
    
    # left: 가장 왼쪽 원소부터 스택에 넣기          
    elif S == 'left':
        for r in range(N):
            # 스택에 집어 넣으면서 같은 숫자 있으면 더해서 합쳐주기
            stack = [0] * N         # N칸 스택 생성
            top = -1
            top_fusion = False      # top원소가 합쳐진 원소인지 아닌지 여부
            for c in range(N):
                stacking()
            # 완성된 스택을 final arr에 넣어주기
            for c in range(N):
                final_arr[r][c] = stack[c]
    
    # right: 가장 오른쪽 원소부터 스택에 넣기
    else:
        for r in range(N):
            # 스택에 집어 넣으면서 같은 숫자 있으면 더해서 합쳐주기
            stack = [0] * N         # N칸 스택 생성
            top = -1
            top_fusion = False      # top원소가 합쳐진 원소인지 아닌지 여부
            for c in range(N-1, -1, -1):
                stacking()
            # 완성된 스택을 final arr에 넣어주기
            for c in range(N):
                final_arr[r][N-1-c] = stack[c]
                
    # 최종 결과 출력
    print(f'#{tc}')
    for i in range(N):
        print(*final_arr[i])