'''
세 줄 짜리 docstring 만들기
주석은 코드에 영향을
주지 않는다
'''

import math

def get_area (radius):
    '''
    세 줄 짜리 docstring 만들기
    주석은 코드에 영향을
    주지 않는다
    '''

    area = math.pi * math.pow(radius, 2)
    return area

radius = 1.5

print('반지름:', radius)

area = get_area(radius)

print('원의 넓이:', area)

print('함수설명서:', get_area.__doc__)


help(get_area)


'''
변수는 값을 담는 공간이다
'''

'''
지시문과 겹치면 안되고
숫자부터 시작하면 안되고
특수문자 포함하면 안되고
공백 포함하면 안된다
'''

x = 15

y = 'food'

print ( '숫자:', x)

print ('영어:', y)

address = ''' 서울시 영등포구
우편번호 43256
도로명 주소
'''

print ('주소:', address)

x , y, z = '사과' , '귤', '배'

print('첫번째 과일:', x)
print('두번째 과일:', y)
print('세번째 과일:', z)


x = y = z = '감'

print('계절 과일:', x)
print('계절 과일:', y)
print('계절 과일:', z)


'''
변수에는 타입이 있다

문자열(str): 문자열 저장
정수(int): 숫자를 저장
실수(float): 소수점있는 숫자를 저장
불린(bool): 참/거짓(True/False)를 저장
'''

text = 'Hi How are you'
print('문자열:', text)
print('문자열 타입:', type(text))

integer = 15
number = 30.4

'''
리스트 list 여러 값을 순서대로 저장
튜플 tuple 리스트와 비슷하지만 수정 불가능
딕셔너리 dict 키와 값의 쌍으로 저장
세트 set 중복없이 저장 순서 없음
'''

musical_list = [   ]
musical_tuple = (  )
musical_dict = {  :   }
musical_set = {   }