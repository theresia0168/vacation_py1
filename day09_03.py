aa=[10,20,30,40]

print(aa[0])
print(aa[1:3])
print(aa[3:])

ss="파이썬최고"
print(ss[0])
print(ss[1])
print(ss[2])
print(ss[1:3])
print(ss[3:])

ss1="파이썬은 재미있어요"

ss1len = len(ss1)
for i in range(0,ss1len):
    print(ss1[i]+'$', end="")
print("")
outstr=""
for i in rnage(0,ss1len):
    outstr=outstr+ss1[ss1len-(i+1)]
print(outstr)
