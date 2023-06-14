'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값을 비교한다.
몇번 만에 맞췄는지 알려준다.

사용자에게 힌트를 준다
사용자가 입력한 값이 랜덤 값보다 크면 숫자는 작다라고 한다.
사용자가 입력한 값이 랜덤 값보다 작으면 숫자는 크다라고 한다.

사용자가 값을 입력하여 힌트를 받을 때 마다 count를 증가한다.

맞출 때까지 한다. 한번
'''
# 알고리즘
# 1. 무한반복하기
#       1) 컴퓨터 랜덤 수 생성
#       2) 사용자로부터 정수 입력 받기
#       3) 입력받은 수와 랜덤 수 비교
#               a. 랜덤수가 더 크거나 작으면 힌트
#               a. 맞추면 시도횟수 출력
#                       b. 프로그램 종료
# 

import random as r
com_int=r.randint(1,30)
cnt=1
start=input("게임을 할까요?(yes or no) : ")
if start.lower()=='yes' :
    while True :
        user_int=int(input("숫자를 입력하세요.(1 ~ 30) : "))
        if user_int>com_int :
            print("랜덤 값이 더 작습니다.")
            cnt+=1
        elif user_int<com_int :
            print("랜덤 값이 더 큽니다.")
            cnt+=1
        else :
            print("정답입니다!")
            print("시도 횟수 :",cnt)
            break
