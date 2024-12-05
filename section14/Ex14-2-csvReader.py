'''
파일명: Ex14-2-csvReader

CSV(comma-seperated values)
    필드를 쉼표(,)로 구분한 텍스트 파일

'''

member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break

        member = line.split(',')
        member_list.append(member)

print(member_list[0][0]

#오류있음 깃허브 확인필요





























