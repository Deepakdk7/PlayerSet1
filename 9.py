ax=input().split()
a=int(ax[0])
b=int(ax[1])
c=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c=c+1
print(c)
