a=int(input())
x=[]
y=[]
for i in range(a):
    s1,s2=input().split()
    t=s1+' '+s2
    x.append(t)
    s1=int(s1)
    if 'g' in s2:
        s1=s1
    elif 'p' in s2:
        s1=s1*16380
    elif 't' in s2:
        s1=s1*(10**6)
    if len(s2)>1:
        if 'm' in s2:
            s1*=(10**(-3))
        if 'k' in s2:
            s1*=(10**3)
        if 'M' in s2:
            s1*=(10**6)
        if 'G' in s2:
            s1*=(10**9)
    y.append(s1)
while x!=[]:
    q=y.index(min(y))
    print(x[q])
    x.remove(x[q])
    y.remove(y[q])
