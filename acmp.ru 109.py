def convert(n,d):
    x=str(n//d)
    ans=str(n//d)+'.'
    b=str(n//d)+'.'
    l={}
    index=0
    n=n%d
    l[n]=index  #Follow us for more.
    t=False     #instagram.com/amirymax
    while t==False:
        if n==0:
            break
        digit=n*10//d
        n=n*10-(n*10//d)*d
        if n not in l:
            ans+=str(digit)
            index+=1
            l[n]=index
            t=False
        else:
            ans+=str(digit)+')'
            ans=ans[:l.get(n)+len(ans[:ans.index('.')+1])]+'('+ans[l.get(n)+len(ans[:ans.index('.')+1]):]
            t=True
    if ans==b:
        return x
    else:
        return ans

a,b=map(int,input().split('/'))
print(convert(a,b))