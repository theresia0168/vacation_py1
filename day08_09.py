alist=[[10,20,30,40],
       [50,60,70,80],
       [90,100,110,120]]

sum1=0
for i in range(len(alist)):
    for j in range(len(alist[i])):
        sum1+=alist[i][j]
print("sum = %d"%sum1)

sum=0
for x in alist:
    for y in x:
      sum+=y
print("sum = %d"%sum)
