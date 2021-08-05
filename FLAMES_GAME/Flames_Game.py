##FLAMES
panter1=str(input("Enter your name1:-"))
panter2=str(input("Enter your name2:-"))
for i in panter1:
    for j in panter2:
        if i==j:
            panter1=panter1.replace(i,"",1)
            panter2=panter2.replace(j,"",1)
            break
c=len(panter1+panter2)
if c>0:
    l=["Friends","Lovers","Affectionate","Marrige","Enemies","Siblings"]
    while len(l)>1:
        r=c%len(l)
        i=r-1
        if i>=0:
            left=l[:i]
            right=l[i+1:]
            l=right+left
        else:
            l=l[:len(l)-1]
    print("relationship is:-",l[0])
else:
    print("Enter a different name")
