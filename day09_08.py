instr="   한글 Python 프로그래밍 "
outstr=""

for i in range(0,len(instr)):
    if instr[i]!=' ':
        outstr+=instr[i]

print("원래 문자열 ==>"+"["+instr+"]")
print("공백 삭제 문자열 ==>"+"["+outstr+"]")

instr="<<<파<<이>>썬>>>"
outstr=""
for i in range(0,len(instr)):
    if instr[i]!='<'and instr[i]!='>':
        outstr+=instr[i]
print("원래 문자열 ==>"+"["+instr+"]")
print("공백 삭제 문자열 ==>"+"["+outstr+"]")

instr='열심히 파이썬 공부 중입니다'
outstr=instr.replace("파이썬","Python")

print("원래 문자열 ==>"+"["+instr+"]")
print("공백 삭제 문자열 ==>"+"["+outstr+"]")
