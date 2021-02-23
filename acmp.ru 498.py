from itertools import *
n,k=map(int,input().split())
a=[i for i in range(1,n+1)]
def check(a,k):
   x=0
   for i in range(len(a)-1):
      if abs(a[i]-a[i+1])<=k:
         x+=1
   if x==len(a)-1:
      return 1
   else:return 0
s=0
x=permutations(a)
for i in x:
   s+=check(i,k)
print(s)
   
