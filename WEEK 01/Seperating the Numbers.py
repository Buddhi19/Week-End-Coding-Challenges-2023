t=int(input())

def beautiful(s):
    digit=1
    substring=""
    while True:
        substring=s[:digit]
        i=digit
        last_added=int(s[:digit])
        while len(substring)<len(s):
            substring+=str(last_added+1)
            # print(last_added)
            last_added+=1
        # print(substring)
        
        if(substring==s and len(s)!=1):
            return "YES "+s[:digit]
        digit+=1
        if(digit>=len(s)):
            break
    return "NO"

for _ in range(t):
    s=input()
    ans=beautiful(s)
    print(ans)