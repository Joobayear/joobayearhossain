li=[12,78,23,4,5,12,23]
li1=[]
for x in range(0,len(li),1):
    for y in range(x+1,len(li),1):
        if li[x]==li[y]:
            li1.append(li[x])
a=set(li)
b=set(li1)
n=a.difference(b)
print(n)


      
