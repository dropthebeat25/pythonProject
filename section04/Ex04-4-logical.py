'''
파일명: Ex04-4-logical.py

논리 연산자
    참/ 거짓을 판단하는 연산자
    and: 둘 다 True일 때만 True
    or : 하나라도 True 이면 True
    not: True <-> False 반전

'''

a = 10
b = 0
print(f'{a} > 0 and {b} > 0: {a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0: {a > 0 or b > 0}')

print(True and False)
print(True or False)

print(f'not {a}: {not a}')
print(f'not {b}: {not b}')

print(not True)
print(not False)


'''
a = 10
b = 0
print(f'not {a}: {not a}')
print(f'not {b}: {not b}')

not 연산자
not 연산자는 논리 부정(logical negation) 연산자로, 값의 Boolean(True/False) 상태를 반전합니다:

참(Truthy) 값 → False
거짓(Falsy) 값 → True
Python에서 다음과 같은 값은 Falsy로 간주됩니다:

숫자: 0, 0.0
None: None
빈 값: '' (빈 문자열), [] (빈 리스트), {} (빈 딕셔너리)
논리값: False
이 외의 값은 모두 Truthy로 간주됩니다.
'''





