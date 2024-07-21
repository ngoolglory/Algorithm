import sys
sys.stdin = open("C:/Users/82108/Downloads/input.txt", "r")

TC = int(input())
num_lst = list(map(int, input().split()))

num_lst.sort()  # 입력 받은 숫자 리스트 정렬
median_num = num_lst[len(num_lst) // 2]  # 총 갯수를 몫으로 나눈 값이 인덱스인 값 찾기
print(median_num)