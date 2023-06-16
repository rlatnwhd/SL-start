'''
컴퓨터공학부 202395007 김수종

사이렌 오더를 통해 음료를 미리 예약하는 프로그램을 만드시오.
메뉴는 아메리카노 2500원
1. 카페라떼 3000원
2. 바닐라 라떼 3000원입니다
3. 메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을
함수로 작성하시오
선택한 메뉴는 인수로 전달되어
가격이 결과 값으로 반환되는 함수로 작성하시오.


사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''

def menu(num) :
    global name, price
    if num==1 :
        name="아메리카노"
        price="2500"
        return name, price
    elif num==2 :
        name="카페라떼"
        price="3000"
        return name, price
    elif num==3 :
        name="바닐라 라떼"
        price="3000"
        return name, price
    else :
        name="none"
        price="none"
        return name, price

print("0. 종료")
print("1. 아메리카노")
print("2. 카페라떼")
print("3. 바닐라 라떼")
while True :
    num=int(input("메뉴 번호를 입력하세요. : "))
    if num==0 :
        print("프로그램을 종료합니다.")
        break
    menu(num)
    if name!='none' and price!="none" :
        print("{}의 가격은 {}원 입니다.".format(name,price))
    else :
        print("메뉴가 없습니다.")
    