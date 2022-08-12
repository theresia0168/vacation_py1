int1 = int(input("첫번째 값 : "))
int2 = int(input("두번째 값 : "))
int3 = int(input("세번째 값 : "))

i=int1
hap=0
while(i<=int2):
    if i%int3==0:
        hap+=i
    i+=1
print ("%d의 배수의 합 : %d"%(int3, hap));print("")

i=int1
hap=0
while(i<=int2):
    i+=1
    if i%int3==0:
        hap+=i
print ("%d의 배수의 합 : %d"%(int3, hap));print("")
