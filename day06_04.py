for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print("")

print("")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("")

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print("*",end="")
    print("")

print("")

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("")

print("")

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,i*2,1):
        print("*",end="")
    print("")
