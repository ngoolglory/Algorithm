import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    full_date = input()  # 8자리의 날짜 받기
    # 년, 월, 일 파싱
    year = full_date[:4]
    month = full_date[4:6]
    day = full_date[6:]
    
    print(f'#{tc} ', end='')  # test case 먼저 출력
    
    if int(day) < 1:  # day가 1보다 작으면
        print(-1)  # -1 출력
        continue  # 다음 test case로 넘어가기
    
    if int(month) >=1 and int(month) <= 12:  # 월이 유효하면
        if int(month) in [4,6,9,11]:  # 30일까지 있는 달이면
            if int(day) > 30:  # 30일보다 크면
                print(-1)  # -1 출력
                continue  # 다음 test case로 넘어가기
        elif int(month) == 2:  # 2월이면
            if int(day) > 28:  # 28일보다 크면
                print(-1)  # -1 출력
                continue  # 다음 test case로 넘어가기
        else:  # 31일까지 있는 달이면
            if int(day) > 31:  # 31일보다 크면
                print(-1)  # -1 출력
                continue  # 다음 test case로 넘어가기
    else:  # 월이 유효하지 않으면
        print(-1)  # -1 출력
        continue  # 다음 test case로 넘어가기
    
    # 모든 조건에 대해 유효한 경우
    print(year+'/'+month+'/'+day)  # 중간에 '/'를 넣어 출력