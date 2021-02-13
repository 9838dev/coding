# count distinct element in every window

from collections import defaultdict
def count_distinct(arr,n,k):
    d=defaultdict(lambda:0)
    l=[]
    count=0
    for i in range(k):
        if d[arr[i]] == 0:
            count+=1
        d[arr[i]]+=1
    j=0
    l.append(count)
    for i in range(k,n):
        if d[arr[i-k]] == 1:
            count-=1
        d[arr[i-k]]-=1
        if d[arr[i]] == 0:
            count+=1
        d[arr[i]]+=1
        l.append(count)
    print(l)

arr=[1,2,1,3,4,3,2,5]
k=4
count_distinct(arr,len(arr),k)