instr='Python을 열심히 공부 중'

str1 = instr.split()

print(str1)

instr='하나:둘:셋:넷:다섯:여섯'
str2=instr.split(':')
print(str2)

instr='하나\n둘\n셋\n넷\n다섯\n여섯'
str3=instr.splitlines()
print(str3)

instr=input("날짜(연-월-일) 입력 ==>")
ssList = instr.split("-")

