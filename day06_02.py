i=0
k=0

guguLine=""

for i in range(2,10):
    guguLine = guguLine + ("# %d단 #"%i)

print(guguLine)

for i in range(1,10):
    guguLine = ""
    for k in range(2,10):
        guguLine = guguLine + str("%2dX%d=%2d"%(k,i,k*i))

    print(guguLine)
