'''
컴퓨터공학부 202395007 김수종

랜덤으로 10명의 학생의 키와 몸무게를 생성하여 파일에 저장
'''
import random as r

f_name=list("김이박차성천남소조차홍서")
s_name=list("소혜진수빈이서정소연태유진민환호경구재표인현나경준동진")

with open("info.txt","w") as file:
    for i in range(10):
        name=r.choice(f_name) + r.choice(s_name) + r.choice(s_name)
        weight=r.randrange(40, 100)
        height=r.randrange(140, 200)
        
        file.write("{}, {}, {} \n".format(name, weight, height))

