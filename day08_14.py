singer = {}
singer['이름']='TWICE'
singer['구성원 수']=9
singer['데뷔']='서바이벌 식스틴'
singer['대표곡']='SIGNAL'

for key in singer.keys():
    print("%s --> %s"%(key,singer[key]))
print("")

singer1 = {}
singer1['이름']='구름다리'
singer1['구성원 수']=10
singer1['데뷔']='서바이벌 팀싱어송대회'
singer1['대표곡']='구름자전거'

for key in singer1.keys():
    print("%s --> %s"%(key,singer1[key]))
print("")

singer1['구성원 수]']=11
for key in singer1.keys():
    print("%s --> %s"%(key,singer1[key]))

alist = [singer, singer1]
print(alist[0])
print(alist[1])

