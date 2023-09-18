def breakingRecords(scores):
    count_min=0
    count_max=0
    mins=scores[0]
    maxs=scores[0]
    for i in range(1,len(scores)):
        if scores[i]>maxs:
            count_max+=1
            maxs=scores[i]
        if scores[i]<mins:
            count_min+=1
            mins=scores[i]
            
    return [count_max,count_min]

n=int(input())

arr=list(map(int,input().split()))

print(*breakingRecords(arr))