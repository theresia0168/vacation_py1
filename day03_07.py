str1="10.10"
str2="10.11"
str3="10.12"

print(str1+str2+str3+str(10+20))
print((str1*2)+(str2*2)+(str3*2))

f1=float(str1)
f2=float(str2)
f3=float(str3)
print("%2.2f"%(f1+f2+f3))

i1=int("10")
i2=int("20")
i3=int("30")
print("%d"%(i1+i2+i3))

print("i1+i2=%d"%(i1+i2), "i1+i2+i3=%d"%(i1+i2+i3))
print("i1=%d i2=%d i3=%d"%(i1,i2,i3))

print("str1=%s, str2=%s, str3=%s"%(str1, str2, str3))
print("f1=%2.2f, f2=%2.2f, f3=%2.2f"%(f1, f2, f3))

name="안채혁"
age=24
address="Busan Geumgang-ro 503"
print("이름 : %s"%name,"나이 : %d"%age,"주소 : %s"%address)
