ax=input()
c=[]
d=[]
for i in range(0,len(ax)):
    if i%2==0:
        c.append(ax[i])
    else:
        d.append(ax[i])
for i in range(0,len(ax)//2):
    print(d[i],end="")    
    print(c[i],end="")
