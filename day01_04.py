#문자열을 입력 받아 숫자로 변경, 숫자를 입력. 여기서 입력된 값은 문자로 저장됨
#문자로 지정된 값을 int 함수를 사용하여 숫자로 변경

a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

result = a + b
print(a, "+", b, "=", result)

result = a - b
print(a, "-", b, "=", result)

result = a * b
print(a, "*", b, "=", result)

result = a / b
print(a, "/", b, "=", result)
