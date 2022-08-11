for i in range(1,101,1):
    if(i%2)==1:
        print("%2d"%i, end = " ")
    if(i%10)==9:
        print("")
print("")
for i in range(1,101,2):
    if(i%2)==1:
        print("%2d"%i, end = " ")
    if(i%10)==9:
        print("")
print("")
for i in range(1,101,1):
    if(i%2)==0:
        print("%3d"%i, end = " ")
    if(i%10)==0:
        print("")
