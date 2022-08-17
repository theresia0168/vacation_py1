#dictionary
dic1 = {1:'a',2:'b',3:'c'}

print(dic1)

dic2 = {'a':1,'b':2,'c':3}

print(dic2)
print(dic1[1])
print(dic1[3])
print(dic2['b'])

print(type(dic1[1]))
print(type(dic2['a']))

value = dic2['a']+dic2['b']+dic2['c']
print(value)
strvalue = dic1[1]+dic1[2]+dic1[3]
print(strvalue)
