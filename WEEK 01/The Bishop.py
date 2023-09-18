r1,c1,r2,c2=map(int,input().split())

if r1==r2 and c1==c2:
    print(0)
elif(r1-r2==c1-c2):
    print(1)

elif((c1+r1)%2==(c2+r2)%2):
    print(2)
else:
    print(-1)