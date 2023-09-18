def winner(arr,n):
    arr_copy=list(dict.fromkeys(arr))
    if len(arr_copy)==n:
        return "First"
    else:
        if len(arr)%2==0:
            return "Second"
        else:
            return "First"

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(winner(arr,n))