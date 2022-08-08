#변수
boolVar = True  #True의 T는 항상 대문자
intVar = 0      #정수
floatVar = 0.0  #실수
strVar = ""     #문자열

print(type(boolVar))
print(type(intVar))
print(type(floatVar))
print(type(strVar))

#변수의 첫 번째 자리에는 숫자가 올 수 없음 ex) 3boolVar
#_(언더바)는 가능하나 (ex. _boolVar) 지양하는 것이 좋다
#두 번째 자리부터는 숫자 혹은 언더바를 사용해도 무방하다
#예약어는 변수로 사용해서는 안된다
#True, False, None, and, not 등등 

boolVar = False
intVar = 100
floatVar = 123.45
strVar = "안녕하세요"

print(boolVar)
print(intVar)
print(floatVar)
print(strVar)

floatVar = intVar + floatVar
print(floatVar, type(floatVar))
