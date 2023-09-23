t=int(input())

def answer(arr,n):
    nn=len(arr)
    res = nn*(nn+1)//2
    # print(res)
    all=list(dict.fromkeys(list(arr)))
    # print(all)
    if len(all)==26:
        return -1
    if len(arr)==len(all):
        return 0
    return len(arr)-len(all)
    
    

for _ in range(t):
    n=int(input())
    arr=input()
    print(answer(arr,n))