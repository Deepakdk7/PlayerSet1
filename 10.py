ax=input().split()
a=ax[0]
b=ax[1]
c=0
for i in range(0,len(a)):
    if a[i]!=b[i]:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
