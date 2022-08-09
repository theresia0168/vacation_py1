a=2
b=3
c=4
#(a+c)-b
print((a+c)-b)

#연산을 하시오 (b-a)*c
print((b-a)*c)

#(a+c)-b <-- restore in sum1 and print
sum1 = (a+c)-b
print("sum1 =", sum1)
sum2 = (-a)+(-b)+(-c)
print("sum2 =", sum2)
sum3 = ((b-a)*(c-a))
print("sum3 =", sum3)
sum4 = (((a*b)%c)+((a*b)//c))
print("sum4 =", sum4)

#sum1 + sum2 + sum3 + sum4 = ?
print("sum1 + sum2 + sum3 + sum4 =", sum1 + sum2 + sum3 + sum4)

a=2
b=2
c=2
print("a>>2", a>>1)
print("a<<2", a<<1)
print("result1", ((a>>1)*b)+c)
