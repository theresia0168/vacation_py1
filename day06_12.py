n1 = int(input("첫번째 값을 입력하시오 "))
n2 = int(input("두번째 값을 입력하시오 "))

i = n1
hap=0

while i<=n2:
    hap+=i
    i+=1

print("%d에서 %d까지의 합 : %d"%(n1, n2, hap))


hap=0
i=n1
for i in range(n1, n2+1, 1):
    print(i,end=" ")
    hap+=i
print("")
print("%d에서 %d까지의 합 : %d"%(n1, n2, hap))
