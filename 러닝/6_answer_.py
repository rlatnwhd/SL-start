
studant=[]

while True :
    menu = int(input("작업 선택 : "))
    if menu == 1 :
        print("1. 학생 조회 : ", studant)
    elif menu == 2 :
        studant.append(input("2. 학생 추가 : "))
    elif menu == 3 :
        del_student=input("3. 삭제 할 학생 입력 : ")
        if studant.count(del_student) == 0 :
            print("삭제할 학생이 없습니다. 다시 입력하세요!")
            continue
        else :
            studant.remove(del_student)
    elif menu == 0 :
        print("프로그램을 종료합니다.")
        break