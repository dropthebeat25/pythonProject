'''docstring
    파이썬 코드(모듈, 함수, 클래스 등)의
    첫 부분에 문자열("""...""")로 작성하는
    문서화 주석입니다.'''

import math

def get_area(radius):
    """
    원의 넒이를 계산하는 함수
    :param radius: 반지름
    :return: 원의 넓이
    """
    area = math.pi * math.pow(radius, 2)
    return area

radius = 1.5

print('반지름', radius)

area = get_area(radius)

print('원의 넓이', area)

print('함수설명서', get_area.__doc__)

help(get_area)