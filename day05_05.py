input1 = int(input("수를 입력하세요"))

if input1%2 == 0:
    input2 = int(input("수를 입력하세요"))
    if input2%2 == 0:
        print("두 수가 모두 짝수입니다")
    else:
        input3 = int(input("수를 입력하세요"))
        sum = input1 + input2 + input3
        print("세 수의 합은 %d"%sum)
else:
    print("입력된 값은 홀수입니다")
