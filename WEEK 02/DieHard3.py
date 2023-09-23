t=int(input())


gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

for _ in range(t):
    a,b,c=map(int,input().split())
    if max(a,b)<c:
        print("NO")
    elif max(a,b)==c or min(a,b)==c:
        print("YES")
    elif c%gcd(a,b)==0:
        print("YES")
    else:
        print("NO")