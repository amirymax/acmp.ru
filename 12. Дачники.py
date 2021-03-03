def tri(a,b,c):
    return abs(0.5*((b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])))

n=int(input())
k=0
l=10e-8
for i in range(n):
    x,y,x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    p,a,b,c,d=[x,y],[x1,y1],[x2,y2],[x3,y3],[x4,y4]
    s=tri(a,b,c)+tri(b,c,d)
    persons=tri(a,b,p)+tri(b,c,p)+tri(c,d,p)+tri(d,a,p)
    if persons-s<=l:
        k+=1
print(k)