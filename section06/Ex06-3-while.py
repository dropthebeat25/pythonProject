'''
파일명:Ex06-3-while


'''

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)

my_list.pop()
print(my_list)





''''

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)

0이 입력되면 끝까지 실행한 후 리스트에 추가되고 멈춘다

my_list.pop() 마지막으로 추가된 값 삭제 0이 삭제
print(my_list)

'''













