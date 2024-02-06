li=[6,3,4,5,1,10,2,2,4,6,2,7,8,9,11,12]
long=1
start=0
for i in range(len(li)):
    count=1
    for j in range(i,len(li)-1):
        if(li[j+1]==li[j]+1):
            count+=1
        else : break
    if(count>long):
        start=i
        long=count
print(li[start:start+long])

