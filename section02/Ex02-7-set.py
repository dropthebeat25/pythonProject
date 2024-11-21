'''

파일명 : Ex02-7-set.py

세트(Set)
    - 중복을 허용하지 않는 자료구조
    - 순서가 없음(인덱싱 불가)
    - 집합 연산 가능
'''
from asyncio import eager_task_factory

# 1. 세트 생성과 기본 기능
pokemon_type = {'불꽃', '물', '전기', '풀'}
print('포켓몬 속성:', pokemon_type)

# 2. 세트 수정
fire_type = {'파이리', '마그마', '브케인'}

# 단일추가
fire_type.add('리자몽')
print('단일추가:', fire_type)

# 여러 항목 추가
new_fire = {'마그케인', '볼케니온'}
fire_type.update(new_fire)
print('여러 항목 추가:', fire_type)

#요소 빼오기
removed = fire_type.pop()  #임의 제거 및 반환
print('방출된 포켓몬:', removed)
print('현재 포켓몬:', fire_type)

# 3. 세트 요소 전체 출력
water_type = {'꼬부기', '잉어킹', '라프라스'}

for pokemon in water_type:
    print(pokemon)

list = list(water_type)
print('첫번째:', list[0])


'''
list = [1, 2, 3]
print(list[0])
print(list[1])
print(list[2])

for item in list:
   
    첫번째 실행
    item = list[0]
    print(item)
    두번째 실행
    item = list[1]
    print(item)
    세번째 실행
    item = list[2]
    print(item)
  
    print(item)

'''

#4. 세트 제거 메소드
water_type = {'꼬부기', '잉어킹', '라프라스'}
water_type.remove('잉어킹') #값이 없으면 에러
print('remove 후:', water_type)

water_type.discard('라프라스') #값이 없어도 에러 없음
print('discard 후:', water_type)

water_type.pop() # 임의 제거
print('pop 후:', water_type)

#water_type.pop() #값이 없으면 에러 발생 KeyError: 'pop from an empty set'

'''
속독하고 다독하고 손으로 많이 쓰고
모르겠으면 일단 프린트 해보고 에러 화면도 많이 볼 수록 
실력이 는다'''

new_type = {'메가이브이', '뮤'}
new_type.clear() #전체 제거
print('clear 후:', new_type)
















