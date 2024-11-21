'''리스트(List)
    - 순서가 있는 데이터 집합
    - 중복 허용, 수정 가능
    - 다양한 자료형 포함 가능'''

'''
리스트(List)
순서가 있는 데이터 집합
중복 허용, 수정 가능
다양한 자료형 포함 가능
'''

# 문자열 len()
print('문자열 길이:', len('Hello'))

# 문자열 lem()
print('문자열 길이:', len('Hello'))

# 1. 리스트 생성과 접근
pokemon_list = ['피카츄', '라이츄', '파이리']
print('리스트 전체:', pokemon_list)
print('첫번째 포켓몬:', pokemon_list[0])
print('리스트 길이:', len(pokemon_list))


#1. 리스트 생성과 접근
pokemon_list = ['피카츄', '라이츄', '파이리']
print('리스트 전체:', pokemon_list)
print('첫번째 포켓몬:', pokemon_list[0])
print('리스트 길이:', len(pokemon_list))

'''
print('첫번째 포켓몬 문자열 길이:', len(피카츄))
print('첫번째 포켓몬 문자열 길이:', 3)
'''
print('첫번째 포켓몬 문자열 길이:', len(pokemon_list[0]))
print('테스트:', len(pokemon_list[0:2]))
print(pokemon_list[0:2])
print('테스트:', len(pokemon_list[0:2][1]))
print('테스트2:', pokemon_list[0:2][1])
print('첫번째 포켓몬 문자열 길이:', len(pokemon_list[0].replace( '피카츄', '뮤')))

p2 = ['피카츄', '라이츄']
print(p2[1])


pokemon_list = ['피카츄', '라이츄', '파이리']

print('첫번째 포켓몬 문자열 길이:', len(pokemon_list[0]))
print('테스트:', len(pokemon_list[0:2]))
print(pokemon_list[0:2]) #0번쨰부터 두글자 그러니 0, 1에 해당하는 값이지
print('테스트:', len(pokemon_list[0:2][1]))
print('테스트2:', pokemon_list[0:2][1])
print('첫번째 포켓몬 문자열 길이:', len(pokemon_list[0].replace('피카츄', '뮤')))

p2 = ['피카츄', '라이츄']
print(p2[1])

#2. 리스트 슬라이싱
                 #0          1        2      3      4       5
                 # -6       -5      -4     -3      -2     -1
fruit_list = ['블루베리', '바나나', '사과', '자몽', '체리', '망고']
print(fruit_list[2:4])
print(fruit_list[1:])
print(fruit_list[-3:])
print(fruit_list[::-1]) #역으로 순서 시작할 때 쓰임
print(fruit_list[5:2:-1]) #5번인덱스부터 2번인덱스 앞까지 역순으로
print(fruit_list[:3])
#스텝테스트 -2: ['망고', '자몽', '바나나']
print('스텝테스트 -2:', fruit_list[5:0:-2])

#2. 리스트 슬라이싱
            #    0          1       2      3      4       5
            #   -6          -5     -4      -3     -2      -1
fruit_list = ['블루베리', '바나나', '사과', '자몽', '체리', '망고' ]
print(fruit_list[2:4])
print(fruit_list[1:])
print(fruit_list[-3:])
print(fruit_list[::-1]) #역으로 순서 시작할 때 쓰임
print(fruit_list[5:2:-1]) #5번인덱스부터 2번인덱스 앞까지 역순으로
print(fruit_list[:3])

#3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1, 2, 3, 4, 5]
boolean_list = [True, False, True]
mixed_list = ['문자열', 100, True, 3.14]

#3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1, 2, 3, 4, 5]
boolean_list = [True, False, True]
mixed_list = ['문자열', 100, True, 3.14]

#4. 리스트 수정
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_list[1] = '잠만보' #단일 항목 수정
print('수정된 리스트:',pokemon_list )

#4. 리스트 수정
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_list[1] = '잠만보' #단일 항목 수정
print('수정된 리스트:', pokemon_list)

#5. 범위 수정
evolution_list = ['피카츄', '라이츄', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['라이츄Z', '메가파이리']
print('진화 업데이트:', evolution_list)


#5. 범위 수정
evolution_list = ['피카츄', '라이츄', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['라이츄Z', '메가파이리']
print('진화 업데이트:', evolution_list)

'''리스트 주요 메소드
    - append(): 끝에 항목 추가
    - insert(): 지정 위치에 항목 추가
    - remove(): 항목 제거
    - pop(): 마지막 또는 지정위치 제거하고 반환
    - clear(): 리스트 비우기'''

'''
리스트 주요 메소드
append(): 끝에 항목 추가
insert(): 지정 위치에 항목 추가
remove(): 항목 제거
pop(): 마지막 또는 지정위치 제거하고 반환
clear(): 리스트 비우기
'''
# 1. 리스트 기본 메서드
starter_pokemon = ['피카츄', '파이리', '꼬부기']
starter_pokemon.append('이상해씨') # 끝에 추가
print('스타터 포켓몬', starter_pokemon)

starter_pokemon.insert( 1, '잠만보') # 중간 삽입
print('삽입된 포켓몬:', starter_pokemon)

# 2. 리스트 제거 메서드
legendary_pokemon = ['그라돈', '가이오가', '레쿠쟈', '히드런']
print('전설의 포켓몬:', legendary_pokemon)

legendary_pokemon.remove('히드런') # 값으로 제거
print('방출 후:', legendary_pokemon)

release = legendary_pokemon.pop(1)  # 인덱스 제거
print('현재 남은 포켓몬:', legendary_pokemon)
print('방출된 포켓몬:', release)


#1. 리스트 기본 메소드
starter_pokemon = ['피카츄', '파이리', '꼬부기']
starter_pokemon.append('이상해씨')
print('스타터 포켓몬', starter_pokemon)

starter_pokemon.insert(1, '잠만보')
print('삽입된 포켓몬',starter_pokemon)

# 2. 리스트 제거 메서드
legendary_pokemon = ['그라돈', '가이오가', '레쿠쟈', '히드런']
legendary_pokemon.remove('히드런')
print('방출후', legendary_pokemon)

byebye = legendary_pokemon.pop(1)
print('남은 포켓몬', legendary_pokemon)
print('보낸 포켓몬', byebye)

# 3. 리스트 확장과 초기화
a_team = ['나무지기', '가디안']
b_team = ['불꽃숭이', '팽도리']

a_team.extend(b_team) #리스트 합치기
print('연합팀:', a_team)

c_team = a_team + b_team
print('연합팀2:', c_team)

a_team.clear() # 리스트 비우기
print('리셋된 팀:', a_team)

del a_team # 리스트 객체 삭제
#print(a_team) NameError: name 'a_team' is not defined.

#3. 리스트 확장과 초기화
a_team = ['나무지기', '가디안']
b_team = ['불꽃숭이', '팽도리']

a_team.extend((b_team)) #리스트 합치기
print('연합팀', a_team)

c_team = a_team + b_team
print('연합팀2', c_team)

a_team.clear() #리스트 비우기
print('리셋된 팀:', a_team)

del a_team

#print(a_team)







































