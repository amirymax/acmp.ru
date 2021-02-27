from itertools import permutations as p

def f(a):
    s=''
    if a!=False:
        for i in a:
            s+=i 
        return int(s)
    else:
        return -1

a=input()
b=input()
c=input()
xa=list(p(a))
xb=list(p(b))
xc=list(p(c))
inta=[]
intb=[]
intc=[]

for i in range(max(len(xa),len(xb),len(xc))):
    if i<len(xa):
        if xa[i][0]=='0':
            xa[i]=False
        inta.append(f(xa[i]))
    if i<len(xb):
        if xb[i][0]=='0':
            xa[i]=False
        intb.append(f(xb[i]))
    if i<len(xc):
        if xc[i][0]=='0':
            xc[i]=False
        intc.append(f(xc[i]))
s=0

for i in range(len(inta)):
    for j in range(len(intb)):
        for k in range(len(intc)):
            if i==j==k and len(str(inta[i])
            )==len(str(intb[j]))==len(str(intc[k])):
                if inta[i]+intb[j]==intc[k] and inta[i]!=-1 and \
                     intb[j]!=-1 and intc[k]!=-1:
                    s+=1
print(s%(10**9+7))                                       
#Thanks very much for watching guys.
#Если кто-то знаеть решение, в любом языке, 
#пожалуйства обращайтесь
#instagram.com/amirymax