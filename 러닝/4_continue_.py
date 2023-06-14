'''
continue
'''

#리스트의 값 10개 중에서 10보다 큰 수를 출력하세요.
numbers=[183,7,1,45,923,61,5,35,132,9]

for i in numbers :
    if i >= 10 :
        print(i, end=', ')

print()

print("리스트의 값 중 10보다 큰 수 : continue  사용")

for i in numbers :
    if i < 10 :
        continue
    print(i, end=', ')

print()

print("1~30 사이 수 중에서 7의 배수만 출력하시요 : continue  사용")

for i in range(1,31) :
    if i%7!=0 :
        continue
    print(i, end=', ')
print()