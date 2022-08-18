instr=input("입력 문자열==>")
print("출력 문자열==>",end="")
for i in range(0,len(instr)):
    if instr[i]=='o':
        print('$',end='')
    else:
        print(instr[i],end='')
