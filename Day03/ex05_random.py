# ex05_random.py

# import 모듈 불러오기
import random
# random() 0.0~1.0 사이의 난수 값을 반환
num = random.random()
print(num)
# radint(start,end) start ~ end 정수 랜덤 값을 반환
num2 = random.randint(1,5)
print(num2) 

# 평균 구하기
listA = [70,60,55,75,95,90,80,85,100]
total = 0
for i in listA:
    total += i
ave = total / len(listA)
print(ave)

# * 출력
for i in range(1,6):
    print("*"*i)
    
# 가위,바위,보 게임 만들기
# 사용자로부터 가위,바위,보 중 하나를 입력
# 가위,바위,보가 아니면 잘못 입력하셨습니다.
# 가위,바위,보 중 입력했을때 컴퓨터도 가위,바위,보 중 하나를 랜덤으로 지정
# 각각 비교
rps = input("가위,바위,보 중 하나를 입력해주세요 :")
if rps != '가위' and rps != '바위' and rps != '보':
    print("잘못입력하셨습니다.")
else :
    print("%s를 입력하셨습니다." %rps)
    rpsnum = random.randint(1,3)
    comrps = "가위" if rpsnum == 1 else "바위" if rpsnum ==2 else "보"
    print("컴퓨터는 %s를 냈습니다" %comrps)
    if rps == comrps :
        print('비겼습니다.')
    elif (rps == "가위" and comrps == "보" 
        or rps=="바위" and comrps=="가위" 
        or rps =="보" and comrps=="바위"):
        print("당신이 이겼습니다.")
    else :
        print("컴퓨터가 이겼습니다.")