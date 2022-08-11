age = int(input("나이를 입력하세요"))

if age <= 7:
    print("유아입니다")
elif age >= 8 and age <= 13:
    print("초등학생입니다")
elif age >= 13 and age <= 16:
    print("중학생입니다")
elif age >= 16 and age <= 19:
    print("고등학생입니다")
elif age >= 19 and age <= 25:
    print("대학생입니다")
else:
    print("성인입니다")
