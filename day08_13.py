student1={'학번':1000,'이름':'홍길동','학과':'컴퓨터학과'}
print(student1)

student1['연락처'] = '010-1212-2121'
print(student1)

student1['학과'] = '파이썬학과'
print(student1)

del(student1['학과'])
print(student1)

student1['학과'] = '정보통신학과'
print(student1)

student2={'학번':2000,'이름':'척준경','학과':'파이썬학과','연락처':'010-1122-3322'}
print(student2)

stNum = student1['학번']

stNum2 = student2.get('학번')

print(stNum, stNum2)

stKeyList = list(student1.keys())
stValueList = list(student1.values())

print(stKeyList)
print(stValueList)

for key in student1.keys():
    print("%s-->%s"%(key,student1[key]))
