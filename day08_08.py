atuple=((10,20,30),
        (40,50,60),
        (70,80,90))
print(atuple)

atuple=((10),(20))
print(atuple)

atuple = ((1,2,3),
          (4,5,6),
          (7,8,9))
print(atuple)

for i in range(len(atuple)):
    for j in range(len(atuple[i])):
        print(atuple[i][j],end=" ")
    print("")

sum1=0
for x in atuple:
    for y in x:
        sum1+=y
print("sum = %d"%sum1)

sum1=0
for i in range(len(atuple)):
    for j in range(len(atuple[i])):
        sum1+=atuple[i][j]
print("sum = %d"%sum1)
