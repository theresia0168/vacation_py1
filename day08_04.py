alist = [[10,20],[30,40],[50,60]]

for x in alist:
    for y in x:
        print(y,end=" ")
print("")

for x,y in alist: #비정방형일때는 사용할 수 없는 방법
    print(x,y,end=" ")
print("")

alist = [[10,20,30],[30,40,50],[50,60,70]]

for x,y,z in alist:
    print(x,y,z,end=" ")
