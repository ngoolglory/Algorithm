for i in range(5):  # 0부터 5까지
    lst = ['+' for _ in range(5)]  # '+' 5개로 채워진 리스트 만들기
    lst[i] = '#'  # lst에서 i 인덱스에 해당하는 값을 '#'로 바꾸기
    print(''.join(lst))  # 업데이트 된 리스트 원소를 다 붙여서 문자열로 만들고 출력