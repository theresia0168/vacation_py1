alist=[[10,20],
       [50,60,70],
       [9],
       [30,40],
       [8],
       [82,9,100.0]]
#비정방행렬(list)

print('alist[0][0]=',alist[0][0])
print('alist[0][1]=',alist[0][1])
#print('alist[0][2]=',alist[0][2])

alist1=[[10,20],
        [30,40],
        [50,60],
        [70,80],
        [90,100]]
#정방행렬(list)

sum = 0
for i in alist:
    sum = sum + i
print("Sum of the alist : ",sum)
