a, b = map(int, input().split())
if a == 1 and b == 3:  # A가 가위, B가 보일 때 
    print('A')  # A 승리
elif a == 3 and b == 1:  # A가 보, B가 가위일 때 
    print('B')
elif a < b:  # A가 바위, B가 보일 때
    print('B')  # B 승리
else:  # A가 보, B가 바위일 때
    print('A')