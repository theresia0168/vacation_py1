instr=""
outstr=""
count=0
i=0

instr=input("문자열을 입력하세요")
count=len(instr)

for i in range(0,count):
    outstr=outstr+instr[count-(i+1)]
print("내용을 거꾸로 출력 --> %s"%outstr)
print("내용 출력 --> %s"%instr)
