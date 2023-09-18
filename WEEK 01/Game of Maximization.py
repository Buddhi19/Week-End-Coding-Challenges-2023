n=int(input())
arr=list(map(int,input().split()))

odd=0
even=0
for i in range(0,n,2):
    odd+=arr[i]
    
for i in range(1,n,2):
    even+=arr[i]

if odd==even:
    print(odd+even)
elif odd>even:
    print(even*2)
else:
    print(odd*2)