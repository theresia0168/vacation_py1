alist = [10,20,30,40,50]

print(len(alist))

for x in range(len(alist)):
    print(alist[x],end=" ")
print("")

alist = [[10,20],
         [30,40,50],
         [60,70],
         [10]]

for x in alist:
    for y in x:
        print(y,end=" ")
print("")

for i in range(len(alist)):
    for j in range(len(alist[i])):
        print(alist[i][j],end=" ")
