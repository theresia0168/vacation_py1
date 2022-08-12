i=0
hap=0

while i<=100:
    i+=1
    if i%3==0:
        continue
    hap+=i
print("1에서부터 100까지 3의 배수를 제외한 수의 합 : %d"%hap);print("")

i=0
hap=0

while i<=100:
    i+=1
    if hap>2000:
        break
    hap+=i
print("합이 2000을 넘게 하는 수 : %d"%i);print("")
