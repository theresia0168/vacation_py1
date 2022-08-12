i=0
hap=0

while True:
    print(i,end=" ")
    i+=1
    if i%2==0:
        continue
    hap+=i
    if i==101:
        break
print("");print("합은 %d"%hap);print("")
