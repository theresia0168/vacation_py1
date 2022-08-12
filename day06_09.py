i=0
hap=0

for i in range(1,101):
    hap+=i
    if hap>=1000:
        break
print("1에서~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d"%i);print("")

i=0
hap=0

for i in range(1,101):
    if i%2==0:
        continue
    hap+=i
print("홀수의 합 : %d"%hap);print("")
