'''
컴퓨터공학부 202395007 김수종

학생 정보를 사전에 저장하고
특정 학생의 정보(학번)을 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
2. 학생 정보 입력 - 사전에 저장 (z 키를 누르면 종료 - 무한 반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한 반복)

'''

#학생 정보 저장 사전
student={}
print("::학생 정보 입력::")
while True :
    num=input("학번 입력 : ")
    if num=='z' :
        break
    name=input("이름 입력 : ")
    student[num]=name

print("입력된 정보 - ",student)
    
print("::학생 검색::")
while True :
    find=input("찾고자 하는 학생의 학번을 입력하세요. : ")
    if find in student :
        print("<< 검색 결과 >>")
        print("학번 : {} / 이름 : {}".format(find,student[find]))
        continue
    elif find=="" :
        print("프로그램 종료")
        break
    print("찾고자 하는 학생이 없습니다.")