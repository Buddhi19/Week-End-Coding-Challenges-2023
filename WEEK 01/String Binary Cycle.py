s=input()

def answer(s):
    max_gap=0
    pointer1=0
    for i in range(len(s)):
        if s[i]=="1":
            pointer1=i
            break
    for i in range(len(s)-1,0,-1):
        if s[i]=="1":
            max_gap=len(s)-1-i+pointer1
            break
    index=pointer1+1
    while index<len(s):
        # print(max_gap)
        if s[index]=="1":
            gap=index-pointer1-1
            if gap>max_gap:
                max_gap=gap
            pointer1=index
        index+=1
    return max_gap
    
if(int("0b"+s,2)==0):
    print(-1)
else:
    print(answer(s))
            