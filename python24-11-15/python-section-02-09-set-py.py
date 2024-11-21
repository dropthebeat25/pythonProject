'''세트(Set)
    - 중복을 허용하지 않는 자료구조
    - 순서가 없음(인덱싱 불가)
    - 집합 연산 가능'''

'''
세트(set)
중복을 허용하지 않는 자료구조
순서가 없음(인덱싱불가)
집합 연산 가능'''

# 1. 세트 생성과 기본 기능
pokemon_type = {'불' , '물', '전기', '풀'}
print('포켓몬 타입:', pokemon_type)

# 2. 세트 수정
fire_type = {'파이리', '마그마', '브케인'}

# 단일추가
fire_type.add('리자몽')
print('단일 추가', fire_type)

#여러 항목 추가
new_fire = {'마그케인', '볼케니온'}
fire_type.update(new_fire)
print('여러항목추가', fire_type)

#요소 빼오기

removed = fire_type.pop()  #임의 제거 및 반환
print('방출된 포켓몬', removed)
print('남은 포켓몬', fire_type)

# 3. 세트 요소 전체 출력
water_type = {'꼬부기', '잉어킹', '라프라스'}

for xavi in water_type:
    print(xavi)

list = list(water_type)
print('첫번째:', list[0])









