'''
컴퓨터공학부 202395007 김수종
키와 몸무게로 비만도 계산하기
'''

with open("info.txt","r") as f:
    for line in f :
        (name, weight, height)=line.strip().split(",")

        if (not name) or (not weight) or (not height) :
            continue
        # 비만도 계산
        bmi = int(weight) / ((int(height) / 100) ** 2)
        if bmi >= 25 :
            res="과체중"
        elif bmi >= 10.5 :
            res="정상 체중"
        else :
            res="저체중"
        
        print("\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {:.2f}", "결과 : {}"]).format(name, weight, height, bmi, res))
        print()