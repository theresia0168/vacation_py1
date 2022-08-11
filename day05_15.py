#1~100까지 홀수와 짝수의 합
hap_even = 0
hap_odd = 0

for i in range(1,100,2):
    hap_odd+=i
print("홀수의 합 : %d"%hap_odd)

for i in range(2,101,2):
    hap_even+=i
print("짝수의 합 : %d"%hap_even)
