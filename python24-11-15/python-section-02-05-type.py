'''

컬렉션 타입

- 리스트(list): 여러 값을 순서대로 저장
- 튜플(tuple): 리스트와 비슷하지만 수정 불가능
- 딕셔너리(dict): 키와 값의 쌍으로 저장 (키값과 밸류)
- 세트(set): 중복없이 저장
'''

         # 인덱스   0       1       2
variable_list = ['당근','오이','토마토'] #리스트
variable_tuple = ('당근','오이','토마토') #튜플
variable_dict = {'종류':'채소', '맛': '없음'} #딕셔너리 #키값으로 불러오기
variable_set = {'당근', '오이', '토마토'} #세트 순서 없음, 중복값 없음

print('리스트', variable_list )
print('튜플', variable_tuple )
print('딕셔너리', variable_dict )
print('세트', variable_set )


print('리스트 세번째 값', variable_list[2] )
print('튜플 첫번째 값', variable_tuple[0] )
print('딕셔너리 첫번째 값', variable_dict['종류'])

