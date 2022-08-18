instr=input("날짜(연-월-일) 입력 ==>")

strList = instr.split("-")
ssList = list(map(int,strList))

print("입력한 날짜의 10년 후 ==>",end="")
print(str((ssList[0]+10))+"년",end="")
print(str(ssList[1])+"월",end="")
print(str(ssList[2])+"일",end="")
