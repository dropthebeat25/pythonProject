'''
파일명: Ex06-1-while

반복문
    어떤 수행 작업을 한번이 아니라 계속해서 수행해야 할 때 사용한다.

    1. while 문
        특정 조건을 만족하는 동안 반복해서 수행하는 명령어

        while 조건식:
            반복 수행할 코드

'''

n = 10
while n != 0: # True일때 수행 False 일 떄까지 반복
    print(n)
    n -= 1 # n = n - 1
'''
n = 10
10 != 0 True
10
'''

print(f'while문 끝나고 n의 값: {n} ')

'''n = 10
while True: # True일때 수행 False 일 떄까지 반복 , 무한 루프 돈다
    print(n)
    n -= 1 # n = n - 1
'''





















