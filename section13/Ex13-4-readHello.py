'''
파일명: Ex13-4-readHello
open 함수 모드
    r(read mode): 읽기 전용 모드 / 파일 없으면 에러

'''

'''
     while True:
        str = file.readline() #한 줄씩 읽기
        if not str: #파일 끝에 도달하면 종료
            break

        print(str, end='')'''

#str = file.read() # 전체 읽기
   # str = file.readline() # 한 줄씩 읽기
    #str += file.readline() # 한 줄씩 읽기
    #str += file.readline() # 한 줄씩 읽기
    #str += file.readline() # 한 줄씩 읽기

with open('hello.txt', 'rt', encoding='UTF-8') as file:

    line_list = file.readlines()
    print(line_list)












































