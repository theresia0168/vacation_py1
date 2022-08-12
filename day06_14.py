a=0
b=0
c=0
d=0
hap=0

a=int(input("첫번째 수 : "))
b=int(input("두번째 수 : "))
c=int(input("세번째 수 : "))
d=int(input("네번째 수 : "))
hap=a+b+c+d
print("네 수의 합 : %d"%hap);print("")

aa=[0, 0, 0, 0]
hap=0
aa[0]=int(input("첫번째 수 : "))
aa[1]=int(input("두번째 수 : "))
aa[2]=int(input("세번째 수 : "))
aa[3]=int(input("네번째 수 : "))
hap=aa[0]+aa[1]+aa[2]+aa[3]
print("네 수의 합 : %d"%hap);print("")

hap=0
for i in range(0,4,1):
    hap+=aa[i]
print("네 수의 합 : %d"%hap);print("")
