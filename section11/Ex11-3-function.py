'''
파일명: Ex11-3-function

Return
    함수는 작업을 수행한 결과를 변환(return)할 수 있다.
    반환된 값은 함수 호출한 위치에서 사용할 수 있다.

'''
# 매개변수 없음, 리턴 값 있음
def address():
    str = '''우편번호 12345
    서울시 영등포구 여의도동'''
    return str

result = address()
print(result)

# 매개변수 있음, 리턴 값 있음
def plus(num1, num2):
    return num1 + num2

result = plus(5, 7)
print(result)


'''
def add(a, b):
    print(a + b)  # 결과를 출력하지만 반환하지 않음

result = add(3, 5) #8

def add(a, b):
    return a + b  # 결과를 반환

result = add(3, 5)  # result에 8이 저장됨
print(result)       # 출력: 8
'''





















