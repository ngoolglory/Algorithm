# 스도쿠 판정
import sys
#input = sys.stdin.readline
sys.stdin = open("C:/Users/82108/Downloads/sample_input.txt", "r")

# 스도쿠인지 아닌지 체크
def sudoku_check(arr):
    # 가로 확인
    for r in range(9):
        num_list = [1] + [0]*9      # 0번 인덱스만 1인 10칸 리스트
        # 가로 한 줄 확인
        for c in range(9):
            num_list[arr[r][c]] = 1     # 해당 인덱스 1로 표기
        # 1로 표기 되지 않은 인덱스가 있다면 0 리턴
        if 0 in num_list:
            return 0
        
    # 세로 확인
    for c in range(9):
        num_list = [1] + [0]*9      # 0번 인덱스만 1인 10칸 리스트
        # 세로 한 줄 확인
        for r in range(9):
            num_list[arr[r][c]] = 1     # 해당 인덱스 1로 표기
        # 1로 표기 되지 않은 인덱스가 있다면 0 리턴
        if 0 in num_list:
            return 0
    
    # 3*3 확인
    start_r = 0
    start_c = 0
    for _ in range(9):
        # 시작 컬럼 위치가 9가 되었다는 건 다음 행으로 가야한다는 뜻
        if start_c == 9:
            start_c = 0     # 시작 컬럼 0으로 갱신
            start_r += 3    # 행 다음 칸으로 내리기
        
        num_list = [1] + [0]*9      # 0번 인덱스만 1인 10칸 리스트
        for r in range(start_r, start_r+3):
            for c in range(start_c, start_c+3):
                num_list[arr[r][c]] = 1     # 해당 인덱스 1로 표기
        # 1로 표기 되지 않은 인덱스가 있다면 0 리턴
        if 0 in num_list:
            return 0

        start_c += 3    # 시작 컬럼 다음 칸으로 옮기기
    
    # 한번도 return 0에 안걸렸으면 1 리턴
    return 1
        

for tc in range(1, 1+int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]   # 스도쿠 배열
    answer = sudoku_check(arr)
    print(f'#{tc}', answer)