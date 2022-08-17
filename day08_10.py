alist=((1,2,3,4,5),
       (6,7,8,9),
       (10,))

sum = 0
for x in alist:
    for y in x:
       sum+=y
print("sum = %d"%sum);print("")

sum = 0
for x in range(len(alist)):
    for y in range(len(alist[x])):
       sum+=alist[x][y]
print("sum = %d"%sum);print("")

