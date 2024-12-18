'''
파일명: Ex03-3-format.py

문자열 포매팅
    - % 포매팅: 파이썬 초기부터 있던 방식
    -  format(): 파이썬 2.6부터 도입
    - f-string: 파이썬 3.6부터 도입(현재 권장)

'''

#1. % 포매팅 (레거시)
'''
print() 형식 문자
    %d : 정수 데이터
    %f : 실수 데이터
    %o : 8진수 데이터
    %s : 문자열 데이터
    %c : 문자 하나 데이터
'''
pokemon = '피카츄'
level = 25
hp = 35.5
print('1. % 포매팅')
print('포켓몬: %s' % pokemon)
print('레벨: %d' % level)
print('체력: %f' % hp)
print('체력: %.1f' % hp)
print('%s의 레벨은 %d입니다.' % (pokemon, level))


print('2. format()함수')
print('포켓몬: {}'.format(pokemon))
print('레벨: {}'.format(level))
print('체력: {:.1f}'.format(level))

print('3. f-string')
print(f'포켓몬: {pokemon}')
print(f'레벨: {level}')
print(f'체력: {hp}')
print(f'체력: {hp:.2f}')

# 8진수
#print('%o' % 8)
oct = 0o10
print('%d' % oct)
'''
0o10

Python에서 숫자 앞에 **0o**를 붙이면 8진수를 나타냅니다.
0o10은 8진수로 10을 의미하며, 이는 10진수로 변환하면 8입니다.
'''

#16진수
hex = 0x10
print('%d' % hex)

'''
0x10

Python에서 숫자 앞에 **0x**를 붙이면 16진수를 나타냅니다.
0x10은 16진수로 10을 의미하며, 이는 10진수로 변환하면 16입니다.

'''











