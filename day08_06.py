alist = [[10,20],
         [30,40],
         [50,60]]

i=0

while i < len(alist):
    x,y = alist[i]
    print(x,y,end=" ")
    i+=1
print("")

alist = [10,20]

x,y = alist

print(x,y);print("")

alist[0]=11
alist[1]=22
x,y = alist
print(x,y);print("")
