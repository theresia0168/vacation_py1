i=1
hap=0

while True:
    while (i<=100 and i%2==1):
        hap+=i
        i+=1
    i+=1
    if i==101:
        break
    
print("합은 %d"%hap);print("")
