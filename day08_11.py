atuple = ((1,2),(3,4),(5,6))

btuple = (['a',6],['e','b'],[3,4,4])

ctuple = [(10,20),(30,40)]

btuple[0][0] = 'd'
print(btuple)

ctuple[0] = (40,50)
print(ctuple)

atuple = (1,2,3,4,5,6,7,8,9,10)

print(atuple[1:2]) #slice
print(atuple[1:3])
print(atuple[0::2]) #atuple[0]에서부터 2씩 인덱스 값을 증가

btuple = ('A','B')
ctuple = atuple + btuple
print(ctuple)

dtuple = btuple*3
print(dtuple)
